# E-Gaming Affiliate Scraper

A specialized web scraper designed to find e-gaming operators mentioned on affiliate websites. This tool reads operator names and affiliate site URLs from CSV files and performs intelligent scanning with e-gaming context awareness.

## Features

- **CSV-Based Configuration**: Load operators and affiliate sites from CSV files
- **E-Gaming Context Scoring**: Intelligent scoring system to identify relevant mentions
- **Respectful Scraping**: Built-in delays and request limiting
- **Comprehensive Reporting**: Detailed CSV output and summary reports
- **Flexible CLI Interface**: Command-line tool with multiple options

## Installation

1. Install required dependencies:
```bash
pip install requests beautifulsoup4 pandas
```

2. Place the following files in your working directory:
   - `egaming_affiliate_scraper.py` - Main scraper class
   - `egaming_scraper_cli.py` - Command line interface
   - `egaming_operators.csv` - List of operators to search for
   - `affiliate_sites.csv` - List of affiliate sites to scan

## CSV File Formats

### E-Gaming Operators CSV (`egaming_operators.csv`)
Required columns:
- `name`: Operator name (e.g., "Bet365")
- `website`: Operator website URL
- `license`: Gaming license info
- `country`: Country of operation

Example:
```csv
name,website,license,country
Bet365,https://www.bet365.com,Malta Gaming Authority,Malta
William Hill,https://www.williamhill.com,UK Gambling Commission,United Kingdom
```

### Affiliate Sites CSV (`affiliate_sites.csv`)
Required columns:
- `name`: Site name for identification
- `url`: Base URL to start scraping
- `category`: Type of affiliate site (e.g., "Casino Reviews")
- `priority`: Scanning priority (1=high, 2=medium, 3=low)

Example:
```csv
name,url,category,priority
CasinoGuide,https://www.casinoguide.com,Casino Reviews,1
BettingExpert,https://www.bettingexpert.com,Sports Betting,1
```

## Usage

### Basic Usage
```bash
python egaming_scraper_cli.py
```

### Custom Configuration
```bash
python egaming_scraper_cli.py --operators my_operators.csv --sites my_sites.csv --max-pages 10 --delay 3
```

### High-Quality Results Only
```bash
python egaming_scraper_cli.py --min-score 50 --max-pages 15
```

### Summary Report Only
```bash
python egaming_scraper_cli.py --summary-only
```

## Command Line Options

- `--operators FILE`: CSV file with gaming operators (default: egaming_operators.csv)
- `--sites FILE`: CSV file with affiliate sites (default: affiliate_sites.csv)
- `--output FILE`: Output CSV file for results (auto-generated if not specified)
- `--max-pages N`: Maximum pages to scrape per site (default: 20)
- `--delay N`: Delay between requests in seconds (default: 2.0)
- `--min-score N`: Minimum e-gaming relevance score (0-100, default: 0)
- `--summary-only`: Generate only summary report, no detailed CSV
- `--verbose`: Enable verbose logging

## E-Gaming Context Scoring

The scraper uses an intelligent scoring system (0-100) to determine how relevant each mention is to e-gaming:

- **Base Keywords**: +10 points each for terms like "casino", "poker", "betting", "bonus"
- **Combination Bonuses**: 
  - "casino" + "bonus" = +20 points
  - "sports" + "betting" = +20 points
  - "affiliate" + "commission/partner/referral" = +15 points

Scores ≥50 are considered high-confidence e-gaming related matches.

## Output Files

### Detailed Results CSV
Contains individual matches with columns:
- Operator information (name, website, license, country)
- Match details (found pattern, context, e-gaming score)
- Page information (URL, title, timestamp)
- Affiliate site information (name, category, priority)

### Summary Report JSON
Contains aggregated statistics:
- Total matches and unique operators found
- Top operators and affiliate sites by mention count
- Average e-gaming scores and high-confidence matches
- Breakdown by affiliate site category

## Example Output

```
Starting scan:
  - 20 operators to search for
  - 15 affiliate sites to scan
  - Max 20 pages per site
  - 2.0s delay between requests

Scraping CasinoGuide: https://www.casinoguide.com
Scraping page 1/20: https://www.casinoguide.com
Found mention: Bet365 (score: 85)
...

=== SCAN SUMMARY ===
Total matches found: 127
Unique operators found: 18
Sites with matches: 12
Average e-gaming score: 67.3
High confidence matches (≥50): 89

Top operators found:
  - Bet365: 15 mentions
  - William Hill: 12 mentions
  - 888 Casino: 8 mentions

Scan completed successfully!
```

## Programmatic Usage

```python
from egaming_affiliate_scraper import EGamingAffiliateScraper

# Initialize scraper
scraper = EGamingAffiliateScraper(max_pages_per_site=15, delay=2.0)

# Load data
scraper.load_operators_from_csv('egaming_operators.csv')
scraper.load_affiliate_sites_from_csv('affiliate_sites.csv')

# Perform scraping
matches = scraper.scrape_all_sites()

# Save results
scraper.save_results_to_csv(matches, 'results.csv')
summary = scraper.generate_summary_report(matches)
```

## Best Practices

1. **Respectful Scraping**: Use appropriate delays (2+ seconds) between requests
2. **Quality Over Quantity**: Focus on high-priority affiliate sites first
3. **Score Filtering**: Use `--min-score` to focus on relevant matches
4. **Regular Updates**: Keep operator and site lists current
5. **Legal Compliance**: Respect robots.txt and terms of service

## Troubleshooting

### Common Issues

1. **"No operators loaded"**: Check CSV file format and column names
2. **"No affiliate sites loaded"**: Verify affiliate_sites.csv exists and is formatted correctly
3. **Connection errors**: Increase delay time or check internet connection
4. **Low match counts**: Review operator names in CSV for accuracy

### Performance Tips

- Start with a small number of sites to test configuration
- Use higher priority sites first
- Adjust max-pages based on site size
- Monitor e-gaming scores to refine search terms

## Technical Details

- **Language**: Python 3.6+
- **Dependencies**: requests, beautifulsoup4, pandas
- **Output Formats**: CSV (detailed), JSON (summary)
- **Concurrency**: Sequential scraping with respectful delays
- **Error Handling**: Comprehensive logging and graceful error recovery

## License

This tool is designed for legitimate business intelligence and compliance monitoring. Users are responsible for ensuring their usage complies with all applicable laws and website terms of service.
