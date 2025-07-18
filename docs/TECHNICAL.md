# Technical Documentation

## CSV File Formats

### E-Gaming Operators CSV (`data/egaming_operators.csv`)
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
LeoVegas,https://www.leovegas.com,Malta Gaming Authority,Malta
```

### Affiliate Sites CSV (`data/affiliate_sites.csv`)
Required columns:
- `name`: Site name for identification
- `url`: Base URL to start scraping
- `category`: Type of affiliate site (e.g., "Casino Reviews")
- `priority`: Scanning priority (1=high, 2=medium, 3=low)

Example:
```csv
name,url,category,priority
AskGamblers,https://askgamblers.com,review,1
CasinoMeister,https://casinomeister.com,forum,2
ThePogg,https://thepogg.com,watchdog,1
```

## Command Line Interface

### Basic Usage
```bash
python src/egaming_scraper_cli.py --operators data/egaming_operators.csv --sites data/affiliate_sites.csv
```

### Advanced Options
```bash
python src/egaming_scraper_cli.py \
  --operators data/egaming_operators.csv \
  --sites data/affiliate_sites.csv \
  --output results.csv \
  --max-pages 15 \
  --delay 3 \
  --min-score 50 \
  --verbose
```

### Options
- `--operators`: Path to operators CSV file
- `--sites`: Path to affiliate sites CSV file
- `--output`: Custom output filename
- `--max-pages`: Maximum pages per site (default: 20)
- `--delay`: Delay between requests in seconds (default: 2.0)
- `--min-score`: Minimum relevance score (default: 0)
- `--summary-only`: Generate only summary report
- `--verbose`: Enable detailed logging

## API Reference

### EGamingAffiliateScraper Class

```python
from src.egaming_affiliate_scraper import EGamingAffiliateScraper

# Initialize scraper
scraper = EGamingAffiliateScraper(max_pages_per_site=10, delay=2.0)

# Load data
scraper.load_operators_from_csv('data/egaming_operators.csv')
scraper.load_affiliate_sites_from_csv('data/affiliate_sites.csv')

# Run scraping
matches = scraper.scrape_all_sites()

# Save results
scraper.save_results_to_csv(matches, 'output/results.csv')
```

## Scoring System

The scraper uses an intelligent scoring system to identify relevant mentions:

### Base Score
- Each e-gaming keyword found adds 10 points
- Keywords: casino, poker, slots, betting, bonus, gambling, etc.

### Bonus Points
- Casino + Bonus: +20 points
- Sports + Betting: +20 points
- Affiliate + Commission/Partner/Referral: +15 points

### Score Ranges
- **0-29**: Low confidence (likely false positive)
- **30-49**: Medium confidence (probably relevant)
- **50-100**: High confidence (very likely relevant)

## Output Format

### CSV Results
Each row contains:
- `operator_name`: Gaming operator found
- `operator_website`: Operator's website
- `operator_license`: License information
- `operator_country`: Country of operation
- `found_pattern`: Search pattern that matched
- `url`: Page where mention was found
- `page_title`: Title of the page
- `context`: Text snippet around the mention
- `egaming_score`: Relevance score (0-100)
- `affiliate_site`: Site where mention was found
- `affiliate_category`: Category of affiliate site
- `affiliate_priority`: Priority level of site
- `timestamp`: When the match was found

### Summary Report (JSON)
- `total_matches`: Total number of matches found
- `unique_operators_found`: Number of unique operators found
- `unique_sites_with_matches`: Number of sites with matches
- `average_egaming_score`: Average relevance score
- `top_operators`: Most frequently mentioned operators
- `top_affiliate_sites`: Sites with most matches
- `matches_by_category`: Breakdown by site category
- `high_confidence_matches`: Matches with score ≥50
- `scan_timestamp`: When the scan was performed

## Best Practices

### Respectful Scraping
- Use delays of 2+ seconds between requests
- Limit pages per site (10-20 recommended)
- Monitor for rate limiting or blocks
- Respect robots.txt files

### Data Quality
- Keep operator and site lists updated
- Verify CSV file formats before running
- Review high-scoring matches manually
- Filter results by relevance score

### Performance
- Start with fewer pages per site for testing
- Use appropriate delays based on site responsiveness
- Monitor system resources during large scans
- Consider running during off-peak hours

## Troubleshooting

### Common Issues
1. **Import errors**: Ensure all dependencies are installed
2. **CSV format errors**: Check column names and data format
3. **Network timeouts**: Increase delay between requests
4. **Memory issues**: Reduce pages per site or process sites individually
5. **No results**: Check operator names and site accessibility

### Debugging
Enable verbose logging to see detailed progress:
```bash
python src/egaming_scraper_cli.py --verbose
```

### Support
If you encounter persistent issues:
1. Run `test_setup.py` to verify installation
2. Check error messages for specific issues
3. Verify CSV file formats
4. Test with a smaller dataset first
