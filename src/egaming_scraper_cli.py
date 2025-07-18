#!/usr/bin/env python3
"""
E-Gaming Affiliate Scraper CLI
Command line interface for the specialized e-gaming affiliate scraper
"""

import argparse
import sys
import os
from datetime import datetime
import json

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from egaming_affiliate_scraper import EGamingAffiliateScraper

def main():
    parser = argparse.ArgumentParser(
        description='E-Gaming Affiliate Scraper - Find gaming operators on affiliate sites',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --operators operators.csv --sites sites.csv
  %(prog)s --operators operators.csv --sites sites.csv --max-pages 10 --delay 3
  %(prog)s --operators operators.csv --sites sites.csv --output my_results.csv
        """
    )
    
    parser.add_argument(
        '--operators',
        default='egaming_operators.csv',
        help='CSV file containing gaming operators (default: egaming_operators.csv)'
    )
    
    parser.add_argument(
        '--sites', 
        default='affiliate_sites.csv',
        help='CSV file containing affiliate sites to scan (default: affiliate_sites.csv)'
    )
    
    parser.add_argument(
        '--output',
        help='Output CSV file for results (default: auto-generated with timestamp)'
    )
    
    parser.add_argument(
        '--max-pages',
        type=int,
        default=20,
        help='Maximum pages to scrape per site (default: 20)'
    )
    
    parser.add_argument(
        '--delay',
        type=float,
        default=2.0,
        help='Delay between requests in seconds (default: 2.0)'
    )
    
    parser.add_argument(
        '--min-score',
        type=int,
        default=0,
        help='Minimum e-gaming relevance score to include (0-100, default: 0)'
    )
    
    parser.add_argument(
        '--summary-only',
        action='store_true',
        help='Only generate summary report, no detailed CSV'
    )
    
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Enable verbose logging'
    )

    args = parser.parse_args()
    
    # Validate input files
    if not os.path.exists(args.operators):
        print(f"Error: Operators file not found: {args.operators}")
        print("Please create this file with columns: name,website,license,country")
        return 1
    
    if not os.path.exists(args.sites):
        print(f"Error: Sites file not found: {args.sites}")
        print("Please create this file with columns: name,url,category,priority")
        return 1
    
    # Initialize scraper
    scraper = EGamingAffiliateScraper(
        max_pages_per_site=args.max_pages,
        delay=args.delay
    )
    
    # Load data
    print(f"Loading operators from: {args.operators}")
    scraper.load_operators_from_csv(args.operators)
    
    print(f"Loading affiliate sites from: {args.sites}")
    scraper.load_affiliate_sites_from_csv(args.sites)
    
    if not scraper.operators:
        print("Error: No operators loaded from CSV file")
        return 1
    
    if not scraper.affiliate_sites:
        print("Error: No affiliate sites loaded from CSV file")
        return 1
    
    print(f"\nStarting scan:")
    print(f"  - {len(scraper.operators)} operators to search for")
    print(f"  - {len(scraper.affiliate_sites)} affiliate sites to scan")
    print(f"  - Max {args.max_pages} pages per site")
    print(f"  - {args.delay}s delay between requests")
    print()
    
    # Perform scraping
    try:
        matches = scraper.scrape_all_sites()
        
        # Filter by minimum score
        if args.min_score > 0:
            original_count = len(matches)
            matches = [m for m in matches if m.get('egaming_score', 0) >= args.min_score]
            print(f"Filtered results: {len(matches)}/{original_count} matches above score {args.min_score}")
        
        # Generate file names
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if not args.summary_only:
            output_file = args.output or f"egaming_findings_{timestamp}.csv"
            scraper.save_results_to_csv(matches, output_file)
            print(f"Detailed results saved to: {output_file}")
        
        # Generate summary
        summary = scraper.generate_summary_report(matches)
        summary_file = f"egaming_summary_{timestamp}.json"
        
        with open(summary_file, 'w') as f:
            json.dump(summary, f, indent=2)
        
        print(f"Summary report saved to: {summary_file}")
        
        # Print summary to console
        print(f"\n=== SCAN SUMMARY ===")
        print(f"Total matches found: {summary['total_matches']}")
        print(f"Unique operators found: {summary['unique_operators_found']}")
        print(f"Sites with matches: {summary['unique_sites_with_matches']}")
        print(f"Average e-gaming score: {summary['average_egaming_score']:.1f}")
        print(f"High confidence matches (≥50): {summary['high_confidence_matches']}")
        
        if summary['total_matches'] > 0:
            print(f"\nTop operators found:")
            for operator, count in list(summary['top_operators'].items())[:5]:
                print(f"  - {operator}: {count} mentions")
            
            print(f"\nTop affiliate sites:")
            for site, count in list(summary['top_affiliate_sites'].items())[:5]:
                print(f"  - {site}: {count} matches")
        
        print(f"\nScan completed successfully!")
        return 0
        
    except KeyboardInterrupt:
        print("\nScan interrupted by user")
        return 1
    except Exception as e:
        print(f"Error during scan: {e}")
        return 1

if __name__ == "__main__":
    exit(main())
