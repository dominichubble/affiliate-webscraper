# User Guide

## Getting Started

### Step 1: Launch the Application

- **Double-click `EASY_SETUP.bat`** (first-time setup - run once)
- **Then double-click `START_APPLICATION.bat`** (starts the application)
- The web browser will open automatically at `http://localhost:8501`

### Step 2: Check Your Data

The application will show if your data files are ready:

- ✅ **Gaming operators file found** - Your list of gaming companies
- ✅ **Affiliate sites file found** - Your list of websites to search

### Step 3: Configure Settings

- **Pages per website**: How many pages to check (start with 5-10)
- **Scraping speed**: How fast to work (use "Medium" for best results)
- **Result quality**: What level of results to show

### Step 4: Run the Scraper

- Click "🚀 START SCRAPING"
- Watch the progress bar
- Wait for completion (this may take several minutes)

### Step 5: Download Results

- View the summary of what was found
- Download the full results as a CSV file
- Results are also saved in the `output/` folder

## Understanding Your Results

### What Each Result Means

- **Operator Name**: Which gaming company was mentioned
- **Affiliate Site**: Which website mentioned it
- **Score**: How relevant the mention is (0-100)
- **URL**: The exact webpage where it was found
- **Context**: The text around the mention

### Quality Scores

- **0-29**: Low quality (might be irrelevant)
- **30-49**: Medium quality (probably relevant)
- **50-100**: High quality (very likely relevant)

### Focus On

- Results with scores above 50
- Multiple mentions of the same operator
- Mentions from high-priority affiliate sites

## Settings Explained

### Pages per Website

- **5**: Quick test (good for trying out)
- **10**: Balanced search (recommended)
- **20+**: Thorough search (takes longer)

### Scraping Speed

- **Slow (3 sec)**: Most respectful to websites
- **Medium (2 sec)**: Good balance (recommended)
- **Fast (1 sec)**: Quickest but less respectful

### Result Quality

- **Show all results**: See everything found
- **Medium quality (30+)**: Filter out noise
- **High quality (50+)**: Only very relevant results

## Tips for Success

### Before You Start

1. Make sure your data files are up to date
2. Start with a small test (5 pages per site)
3. Choose medium speed for best results

### During Scraping

1. Be patient - the tool waits between requests
2. Don't close the browser window
3. Check the progress updates

### After Scraping

1. Review results with high scores first
2. Check if the context makes sense
3. Download or save important results

## Troubleshooting

### Browser Doesn't Open

- Manually go to `http://localhost:8501`
- Try a different browser
- Check if Windows Firewall is blocking

### No Results Found

- Try reducing the quality score filter
- Check if your affiliate sites are accessible
- Verify your operator names are correct

### Slow Performance

- Reduce the number of pages per site
- Increase the delay between requests
- Close other applications using internet

### Error Messages

- Check that your CSV files are formatted correctly
- Ensure you have internet connection
- Try restarting the application

## File Management

### Your Data Files

- **`data/egaming_operators.csv`**: Your gaming operators
- **`data/affiliate_sites.csv`**: Your affiliate sites

### Results Files

- **`output/egaming_findings_*.csv`**: Detailed results
- **`output/egaming_summary_*.json`**: Summary reports

### Backup Your Data

- Keep copies of your original CSV files
- Save important results to a separate folder
- Consider version control for your data files

## Best Practices

### Start Small

- Test with 5-10 pages per site first
- Use a small list of sites initially
- Gradually increase scope

### Be Respectful

- Use appropriate delays between requests
- Don't run too many scans simultaneously
- Respect website terms of service

### Quality Control

- Always review high-scoring results
- Check context to confirm relevance
- Keep your data files updated

## Getting Help

### Self-Help

1. Run `test_setup.py` to check if everything works
2. Check this guide for common issues
3. Try with smaller settings first

### Technical Support

If problems persist:

1. Note the exact error message
2. Check what you were doing when it failed
3. Try the troubleshooting steps above
4. Contact technical support with details

---

**Need help getting started?** Double-click `EASY_SETUP.bat` then `START_APPLICATION.bat` and follow the steps!
