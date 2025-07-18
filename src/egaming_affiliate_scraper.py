#!/usr/bin/env python3
"""
E-Gaming Affiliate Scraper
Specialized scraper for finding egaming operators on affiliate sites
Reads operator names and affiliate sites from CSV files
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, urlunparse
import time
import json
import re
import csv
import pandas as pd
from collections import deque
from typing import Set, List, Dict, Optional, Tuple
import logging
from datetime import datetime
import os

class EGamingAffiliateScraper:
    def __init__(self, max_pages_per_site: int = 20, delay: float = 2.0):
        """
        Initialize the e-gaming affiliate scraper
        
        Args:
            max_pages_per_site: Maximum number of pages to scrape per site
            delay: Delay between requests in seconds (higher for respectful scraping)
        """
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
        self.max_pages_per_site = max_pages_per_site
        self.delay = delay
        self.visited_urls: Set[str] = set()
        self.found_matches: List[Dict] = []
        
        # E-gaming specific data
        self.operators: List[Dict] = []
        self.affiliate_sites: List[Dict] = []
        
        # Setup logging
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)
        
        # E-gaming related keywords for enhanced detection
        self.egaming_keywords = [
            'casino', 'poker', 'slots', 'blackjack', 'roulette', 'baccarat',
            'sports betting', 'sportsbook', 'live betting', 'odds',
            'bonus', 'free spins', 'welcome bonus', 'deposit bonus',
            'gambling', 'gaming', 'lottery', 'bingo', 'esports',
            'live casino', 'jackpot', 'progressive', 'tournament',
            'affiliate', 'commission', 'referral', 'partner'
        ]
    
    def load_operators_from_csv(self, csv_file: str) -> None:
        """
        Load e-gaming operators from CSV file
        Expected columns: name, website, license, country
        """
        try:
            if not os.path.exists(csv_file):
                self.logger.warning(f"Operators CSV file not found: {csv_file}")
                return
                
            df = pd.read_csv(csv_file)
            self.operators = df.to_dict('records')
            self.logger.info(f"Loaded {len(self.operators)} operators from {csv_file}")
            
            # Create search patterns for each operator
            for operator in self.operators:
                if 'search_patterns' not in operator:
                    name = operator.get('name', '').lower()
                    # Create variations of the operator name
                    operator['search_patterns'] = [
                        name,
                        name.replace(' ', ''),
                        name.replace(' ', '-'),
                        name.replace(' ', '_')
                    ]
                    
        except Exception as e:
            self.logger.error(f"Error loading operators CSV: {e}")
    
    def load_affiliate_sites_from_csv(self, csv_file: str) -> None:
        """
        Load affiliate sites from CSV file
        Expected columns: name, url, category, priority
        """
        try:
            if not os.path.exists(csv_file):
                self.logger.warning(f"Affiliate sites CSV file not found: {csv_file}")
                return
                
            df = pd.read_csv(csv_file)
            self.affiliate_sites = df.to_dict('records')
            self.logger.info(f"Loaded {len(self.affiliate_sites)} affiliate sites from {csv_file}")
            
        except Exception as e:
            self.logger.error(f"Error loading affiliate sites CSV: {e}")
    
    def normalize_url(self, url: str) -> str:
        """Normalize URL by removing fragments and query parameters"""
        parsed = urlparse(url)
        return urlunparse((parsed.scheme, parsed.netloc, parsed.path, '', '', ''))
    
    def is_valid_url(self, url: str, base_domain: str) -> bool:
        """Check if URL is valid and belongs to the same domain"""
        try:
            parsed = urlparse(url)
            base_parsed = urlparse(base_domain)
            
            # Must have same domain
            if parsed.netloc.lower() != base_parsed.netloc.lower():
                return False
            
            # Skip certain file types
            skip_extensions = ['.pdf', '.jpg', '.jpeg', '.png', '.gif', '.css', '.js', '.ico', '.xml']
            if any(parsed.path.lower().endswith(ext) for ext in skip_extensions):
                return False
            
            return True
            
        except Exception:
            return False
    
    def extract_text_content(self, soup: BeautifulSoup) -> str:
        """Extract clean text content from BeautifulSoup object"""
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
        
        # Get text content
        text = soup.get_text()
        
        # Clean up whitespace
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        
        return text
    
    def find_operator_mentions(self, text: str, url: str, title: str) -> List[Dict]:
        """Find mentions of e-gaming operators in the text"""
        matches = []
        text_lower = text.lower()
        
        for operator in self.operators:
            operator_name = operator.get('name', '')
            search_patterns = operator.get('search_patterns', [])
            
            for pattern in search_patterns:
                if pattern and pattern in text_lower:
                    # Extract context around the match
                    pattern_index = text_lower.find(pattern)
                    start = max(0, pattern_index - 100)
                    end = min(len(text), pattern_index + len(pattern) + 100)
                    context = text[start:end].strip()
                    
                    # Check for e-gaming context indicators
                    egaming_score = self.calculate_egaming_score(context.lower())
                    
                    match = {
                        'operator_name': operator_name,
                        'operator_website': operator.get('website', ''),
                        'operator_license': operator.get('license', ''),
                        'operator_country': operator.get('country', ''),
                        'found_pattern': pattern,
                        'url': url,
                        'page_title': title,
                        'context': context,
                        'egaming_score': egaming_score,
                        'timestamp': datetime.now().isoformat()
                    }
                    matches.append(match)
                    break  # Only count first occurrence per operator per page
        
        return matches
    
    def calculate_egaming_score(self, context: str) -> int:
        """Calculate how likely this context is related to e-gaming (0-100)"""
        score = 0
        for keyword in self.egaming_keywords:
            if keyword in context:
                score += 10
        
        # Bonus points for specific combinations
        if 'casino' in context and 'bonus' in context:
            score += 20
        if 'sports' in context and 'betting' in context:
            score += 20
        if 'affiliate' in context and any(word in context for word in ['commission', 'partner', 'referral']):
            score += 15
            
        return min(score, 100)
    
    def get_page_content(self, url: str) -> Optional[Tuple[str, str, BeautifulSoup]]:
        """Fetch and parse page content"""
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.title.string.strip() if soup.title and soup.title.string else "No Title"
            text_content = self.extract_text_content(soup)
            
            return title, text_content, soup
            
        except Exception as e:
            self.logger.warning(f"Error fetching {url}: {e}")
            return None
    
    def find_links(self, soup: BeautifulSoup, base_url: str) -> List[str]:
        """Find all valid links on the page"""
        links = []
        base_domain = f"{urlparse(base_url).scheme}://{urlparse(base_url).netloc}"
        
        for link in soup.find_all('a', href=True):
            href = link['href'].strip()
            if not href or href.startswith('#'):
                continue
            
            # Convert relative URLs to absolute
            full_url = urljoin(base_url, href)
            normalized_url = self.normalize_url(full_url)
            
            if self.is_valid_url(normalized_url, base_domain):
                links.append(normalized_url)
        
        return list(set(links))  # Remove duplicates
    
    def scrape_affiliate_site(self, site_info: Dict) -> List[Dict]:
        """Scrape a single affiliate site for operator mentions"""
        start_url = site_info.get('url', '')
        site_name = site_info.get('name', 'Unknown Site')
        
        if not start_url:
            self.logger.warning(f"No URL provided for site: {site_name}")
            return []
        
        self.logger.info(f"Starting scrape of {site_name}: {start_url}")
        
        visited_urls = set()
        found_matches = []
        urls_to_visit = deque([start_url])
        pages_scraped = 0
        
        while urls_to_visit and pages_scraped < self.max_pages_per_site:
            current_url = urls_to_visit.popleft()
            
            if current_url in visited_urls:
                continue
            
            visited_urls.add(current_url)
            pages_scraped += 1
            
            self.logger.info(f"Scraping page {pages_scraped}/{self.max_pages_per_site}: {current_url}")
            
            # Get page content
            page_result = self.get_page_content(current_url)
            if not page_result:
                continue
            
            title, text_content, soup = page_result
            
            # Find operator mentions
            matches = self.find_operator_mentions(text_content, current_url, title)
            for match in matches:
                match['affiliate_site'] = site_name
                match['affiliate_category'] = site_info.get('category', 'Unknown')
                match['affiliate_priority'] = site_info.get('priority', 0)
            
            found_matches.extend(matches)
            
            # Find more links to explore
            if pages_scraped < self.max_pages_per_site:
                new_links = self.find_links(soup, current_url)
                for link in new_links:
                    if link not in visited_urls and link not in urls_to_visit:
                        urls_to_visit.append(link)
            
            # Be respectful with requests
            time.sleep(self.delay)
        
        self.logger.info(f"Completed {site_name}: {pages_scraped} pages, {len(found_matches)} matches")
        return found_matches
    
    def scrape_all_sites(self) -> List[Dict]:
        """Scrape all affiliate sites for operator mentions"""
        all_matches = []
        
        for site_info in self.affiliate_sites:
            try:
                site_matches = self.scrape_affiliate_site(site_info)
                all_matches.extend(site_matches)
            except Exception as e:
                self.logger.error(f"Error scraping site {site_info.get('name', 'Unknown')}: {e}")
        
        return all_matches
    
    def save_results_to_csv(self, matches: List[Dict], output_file: str) -> None:
        """Save results to CSV file"""
        if not matches:
            self.logger.warning("No matches to save")
            return
        
        df = pd.DataFrame(matches)
        df.to_csv(output_file, index=False)
        self.logger.info(f"Results saved to {output_file}")
    
    def generate_summary_report(self, matches: List[Dict]) -> Dict:
        """Generate summary report of findings"""
        if not matches:
            return {
                "total_matches": 0, 
                "unique_operators_found": 0,
                "unique_sites_with_matches": 0,
                "average_egaming_score": 0,
                "high_confidence_matches": 0,
                "message": "No matches found",
                "scan_timestamp": datetime.now().isoformat()
            }
        
        df = pd.DataFrame(matches)
        
        summary = {
            "total_matches": len(matches),
            "unique_operators_found": df['operator_name'].nunique(),
            "unique_sites_with_matches": df['affiliate_site'].nunique(),
            "average_egaming_score": df['egaming_score'].mean(),
            "top_operators": df['operator_name'].value_counts().head(10).to_dict(),
            "top_affiliate_sites": df['affiliate_site'].value_counts().head(10).to_dict(),
            "matches_by_category": df.groupby('affiliate_category')['operator_name'].count().to_dict(),
            "high_confidence_matches": len(df[df['egaming_score'] >= 50]),
            "scan_timestamp": datetime.now().isoformat()
        }
        
        return summary

def main():
    """Example usage of the E-Gaming Affiliate Scraper"""
    scraper = EGamingAffiliateScraper(max_pages_per_site=15, delay=2.0)
    
    # Load data from CSV files
    scraper.load_operators_from_csv('egaming_operators.csv')
    scraper.load_affiliate_sites_from_csv('affiliate_sites.csv')
    
    if not scraper.operators:
        print("No operators loaded. Please check egaming_operators.csv file.")
        return
    
    if not scraper.affiliate_sites:
        print("No affiliate sites loaded. Please check affiliate_sites.csv file.")
        return
    
    # Perform the scraping
    print(f"Starting scan of {len(scraper.affiliate_sites)} affiliate sites for {len(scraper.operators)} operators...")
    matches = scraper.scrape_all_sites()
    
    # Save results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"egaming_findings_{timestamp}.csv"
    scraper.save_results_to_csv(matches, output_file)
    
    # Generate and save summary
    summary = scraper.generate_summary_report(matches)
    summary_file = f"egaming_summary_{timestamp}.json"
    with open(summary_file, 'w') as f:
        json.dump(summary, f, indent=2)
    
    print(f"\nScan completed!")
    print(f"Results saved to: {output_file}")
    print(f"Summary saved to: {summary_file}")
    print(f"Total matches found: {summary['total_matches']}")
    print(f"Unique operators found: {summary['unique_operators_found']}")
    print(f"High confidence matches: {summary['high_confidence_matches']}")

if __name__ == "__main__":
    main()
