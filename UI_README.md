# E-Gaming Affiliate Scraper - Web UI

A simple, user-friendly web interface for finding gaming operators mentioned on affiliate websites.

## 🚀 Quick Start

### Option 1: Use the Startup Script (Recommended)
1. Double-click `start_ui.bat`
2. Wait for the web browser to open automatically
3. Start using the scraper through the web interface

### Option 2: Manual Start
1. Install Python packages:
   ```
   pip install -r requirements.txt
   ```
2. Start the web interface:
   ```
   streamlit run app.py
   ```
3. Open your browser to `http://localhost:8501`

## 📋 How to Use

### 1. **Upload Data Files (or use existing ones)**
   - **Operators CSV**: List of gaming operators to search for
     - Required columns: `name`, `website`, `license`, `country`
   - **Affiliate Sites CSV**: List of affiliate websites to scrape
     - Required columns: `name`, `url`, `category`, `priority`

### 2. **Configure Settings**
   - **Max pages per site**: How many pages to scrape from each site (1-50)
   - **Delay between requests**: Time to wait between requests (1-10 seconds)
   - **Minimum relevance score**: Only show results above this score (0-100)

### 3. **Run the Scraper**
   - Click "Start Scraping" when ready
   - Watch the progress bar and status updates
   - Results will be saved automatically to the `output/` folder

### 4. **View Results**
   - See summary statistics (total matches, unique operators, etc.)
   - Preview the top results in the interface
   - Download CSV and JSON files
   - View previous results from the dropdown

## 📊 Understanding Results

### Columns in Results CSV:
- **operator_name**: The gaming operator that was found
- **affiliate_site**: Which affiliate website mentioned it
- **egaming_score**: Relevance score (0-100, higher = more relevant)
- **url**: The specific page where the operator was mentioned
- **context**: Text snippet showing the mention
- **page_title**: Title of the page where it was found
- **timestamp**: When the match was found

### Relevance Score:
- **0-30**: Low confidence - might be false positive
- **31-50**: Medium confidence - likely relevant
- **51-100**: High confidence - very likely relevant

## 📁 File Structure

```
├── app.py                 # Main web UI application
├── start_ui.bat          # Windows startup script
├── requirements.txt      # Python dependencies
├── data/                 # Input CSV files
│   ├── egaming_operators.csv
│   └── affiliate_sites.csv
├── output/               # Results are saved here
│   ├── egaming_findings_*.csv
│   └── egaming_summary_*.json
└── src/                  # Core scraper code
    ├── egaming_affiliate_scraper.py
    └── egaming_scraper_cli.py
```

## 💡 Tips for Best Results

1. **Start Small**: Begin with fewer pages per site (5-10) to test
2. **Be Respectful**: Use delays of 2+ seconds between requests
3. **Quality Data**: Ensure your CSV files have clean, accurate data
4. **Regular Updates**: Keep your operator and site lists updated
5. **Review Results**: Check high-scoring matches manually for accuracy

## 🔧 Troubleshooting

### Common Issues:

**"No operators/sites loaded"**
- Check that your CSV files have the correct column names
- Ensure files are properly formatted (no extra commas, quotes, etc.)

**"Error during scraping"**
- Some websites may block requests - this is normal
- Try reducing the number of pages per site
- Increase the delay between requests

**"Browser doesn't open"**
- Manually go to `http://localhost:8501` in your browser
- Check that no other application is using port 8501

**"Python not found"**
- Install Python from https://python.org
- Make sure to check "Add to PATH" during installation

## 📞 Support

If you encounter issues:
1. Check that all CSV files are properly formatted
2. Ensure you have a stable internet connection
3. Try running with fewer pages per site first
4. Contact your technical team if problems persist

---

**Note**: This tool is designed for legitimate research purposes. Always respect website terms of service and robots.txt files.
