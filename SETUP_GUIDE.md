# Gaming Operator Scraper - Setup Guide for Non-Technical Users

## 🎯 What This Tool Does

This tool searches affiliate websites to find mentions of gaming operators (casinos, betting sites, etc.). It's designed to be simple and user-friendly.

## 🚀 Quick Setup (5 Minutes)

### Step 1: Install Python (if not already installed)
1. Go to https://python.org/downloads/
2. Download the latest Python version
3. **IMPORTANT**: During installation, check "Add Python to PATH"
4. Click "Install Now"

### Step 2: Get Your Data Ready
You need two CSV files in the `data/` folder:

**File 1: `data/egaming_operators.csv`**
- List of gaming operators you want to find
- Required columns: `name`, `website`, `license`, `country`
- Example:
  ```
  name,website,license,country
  Betway,betway.com,MGA,Malta
  888Casino,888casino.com,UKGC,UK
  ```

**File 2: `data/affiliate_sites.csv`**
- List of affiliate websites to search
- Required columns: `name`, `url`, `category`, `priority`
- Example:
  ```
  name,url,category,priority
  AskGamblers,https://askgamblers.com,review,1
  CasinoMeister,https://casinomeister.com,forum,2
  ```

### Step 3: Start the Application
**Option A: Double-click `start_ui.bat`**
**Option B: Right-click `start_ui.ps1` → "Run with PowerShell"**

The application will:
- Install required packages automatically
- Open a web browser with the interface
- Guide you through the rest

## 🖥️ Using the Interface

### Simple UI (Recommended for Beginners)
1. **Check Data Files**: Ensure your CSV files are loaded correctly
2. **Choose Settings**:
   - **Pages per website**: How many pages to check (start with 5-10)
   - **Scraping speed**: How fast to work (Medium recommended)
   - **Result quality**: What quality results to show
3. **Start Scraping**: Click the big "START SCRAPING" button
4. **View Results**: Download the results when done

### Advanced UI (More Options)
- Upload custom CSV files
- More detailed settings
- Real-time progress tracking
- View previous results
- Advanced filtering options

## 📊 Understanding Your Results

### The Results File (CSV)
Each row represents one mention of an operator on a website:

- **operator_name**: Which gaming operator was found
- **affiliate_site**: Which website mentioned it
- **egaming_score**: How relevant the mention is (0-100)
- **url**: The exact page where it was found
- **context**: The text around the mention
- **page_title**: Title of the page

### Quality Scores
- **0-29**: Low quality (might be false positive)
- **30-49**: Medium quality (probably relevant)
- **50-100**: High quality (very likely relevant)

## 🎛️ Settings Explained

### Pages per Website
- **5-10**: Quick test, good for trying out
- **15-20**: Thorough search, recommended
- **25+**: Very thorough, takes longer

### Scraping Speed
- **Slow (3 sec)**: Most respectful to websites
- **Medium (2 sec)**: Good balance (recommended)
- **Fast (1 sec)**: Fastest but less respectful

### Result Quality
- **Show all**: See everything found
- **Medium quality**: Filter out obvious false positives
- **High quality**: Only show very relevant results

## 🔧 Troubleshooting

### "Python not found"
- Reinstall Python from https://python.org
- Make sure to check "Add Python to PATH"
- Restart your computer after installation

### "No data files found"
- Make sure your CSV files are in the `data/` folder
- Check that column names match exactly
- Ensure files are saved as CSV format (not Excel)

### "Browser doesn't open"
- Manually go to http://localhost:8501
- Try a different browser
- Check Windows Firewall settings

### "Scraping stops or errors"
- Some websites may block requests (this is normal)
- Try reducing pages per website
- Increase the delay between requests
- Check your internet connection

### "No results found"
- Check that your operator names are spelled correctly
- Try different affiliate sites
- Reduce the minimum quality score
- Ensure your data files have the right format

## 📁 File Organization

```
Your Folder/
├── start_ui.bat           ← Double-click this to start
├── start_ui.ps1           ← Alternative PowerShell version
├── simple_ui.py           ← Simple interface
├── app.py                 ← Advanced interface
├── requirements.txt       ← Python packages needed
├── data/                  ← PUT YOUR CSV FILES HERE
│   ├── egaming_operators.csv
│   └── affiliate_sites.csv
├── output/                ← Results are saved here
│   ├── egaming_findings_*.csv
│   └── egaming_summary_*.json
└── src/                   ← Core program files
    └── ...
```

## 💡 Tips for Success

1. **Start Small**: Begin with 5-10 pages per site to test
2. **Quality Data**: Make sure your CSV files are clean and accurate
3. **Be Patient**: Scraping takes time to be respectful to websites
4. **Check Results**: Always review high-scoring matches manually
5. **Regular Updates**: Keep your operator and site lists updated

## 🆘 Getting Help

If you run into problems:
1. Check this guide first
2. Try the troubleshooting section
3. Make sure your CSV files are formatted correctly
4. Contact your technical team with specific error messages

## 📋 Example CSV Templates

### Operators CSV Template
```csv
name,website,license,country
Betway,betway.com,MGA,Malta
888Casino,888casino.com,UKGC,UK
LeoVegas,leovegas.com,MGA,Malta
Bet365,bet365.com,UKGC,UK
Unibet,unibet.com,MGA,Malta
```

### Sites CSV Template
```csv
name,url,category,priority
AskGamblers,https://askgamblers.com,review,1
CasinoMeister,https://casinomeister.com,forum,2
ThePogg,https://thepogg.com,watchdog,1
Gambling.com,https://gambling.com,affiliate,3
SlotsTemple,https://slotstemple.com,affiliate,2
```

## 🎉 You're Ready!

Double-click `start_ui.bat` to begin!
