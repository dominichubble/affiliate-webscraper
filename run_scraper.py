#!/usr/bin/env python3
"""
Simple runner script for the E-Gaming Affiliate Scraper
This script demonstrates basic usage and saves all output to the output/ directory
"""

import os
import sys
from datetime import datetime

# Add src directory to path so we can import the scraper
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from egaming_affiliate_scraper import EGamingAffiliateScraper

def main():
    """Run the scraper with default settings"""
    print("E-Gaming Affiliate Scraper")
    print("=" * 50)
    
    # Initialize scraper with reasonable defaults
    scraper = EGamingAffiliateScraper(max_pages_per_site=10, delay=2.0)
    
    # Get paths to data files
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    operators_file = os.path.join(data_dir, 'egaming_operators.csv')
    sites_file = os.path.join(data_dir, 'affiliate_sites.csv')
    
    # Load data from CSV files
    print(f"Loading operators from: {operators_file}")
    scraper.load_operators_from_csv(operators_file)
    
    print(f"Loading affiliate sites from: {sites_file}")
    scraper.load_affiliate_sites_from_csv(sites_file)
    
    # Check if data was loaded
    if not scraper.operators:
        print(f"ERROR: No operators loaded from {operators_file}")
        print("Please ensure the file exists and has the correct format.")
        return 1
    
    if not scraper.affiliate_sites:
        print(f"ERROR: No affiliate sites loaded from {sites_file}")
        print("Please ensure the file exists and has the correct format.")
        return 1
    
    print(f"\nStarting scraping process...")
    print(f"Operators to search for: {len(scraper.operators)}")
    print(f"Affiliate sites to scan: {len(scraper.affiliate_sites)}")
    print(f"Max pages per site: {scraper.max_pages_per_site}")
    print(f"Delay between requests: {scraper.delay} seconds")
    print()
    
    try:
        # Perform the scraping
        matches = scraper.scrape_all_sites()
        
        # Prepare output directory and filenames
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = os.path.join(os.path.dirname(__file__), 'output')
        os.makedirs(output_dir, exist_ok=True)
        
        output_file = os.path.join(output_dir, f"egaming_findings_{timestamp}.csv")
        summary_file = os.path.join(output_dir, f"egaming_summary_{timestamp}.json")
        
        # Save results
        scraper.save_results_to_csv(matches, output_file)
        
        # Generate and save summary
        summary = scraper.generate_summary_report(matches)
        import json
        with open(summary_file, 'w') as f:
            json.dump(summary, f, indent=2)
        
        # Print results
        print(f"\n" + "=" * 50)
        print(f"SCRAPING COMPLETED SUCCESSFULLY!")
        print(f"=" * 50)
        print(f"Results saved to: {output_file}")
        print(f"Summary saved to: {summary_file}")
        print(f"\nSummary:")
        print(f"  Total matches found: {summary['total_matches']}")
        print(f"  Unique operators found: {summary['unique_operators_found']}")
        print(f"  Sites with matches: {summary['unique_sites_with_matches']}")
        print(f"  High confidence matches: {summary['high_confidence_matches']}")
        
        if summary['total_matches'] > 0:
            print(f"\nTop operators found:")
            for operator, count in list(summary['top_operators'].items())[:5]:
                print(f"    {operator}: {count} mentions")
        
        return 0
        
    except KeyboardInterrupt:
        print("\nScraping interrupted by user.")
        return 1
    except Exception as e:
        print(f"ERROR: An error occurred during scraping: {e}")
        return 1

if __name__ == "__main__":
    exit(main())
