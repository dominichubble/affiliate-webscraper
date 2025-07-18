# 🎰 Gaming Operator Scraper - Quick Start Guide

## What This Tool Does
This tool automatically searches affiliate websites to find mentions of gaming operators (casinos, betting sites, etc.). It's designed to be simple and user-friendly.

## ✅ Ready to Use!
Your scraper is now fully set up and ready to use. All required packages are installed and the system has been tested.

## 🚀 How to Start (Choose One)

### Option 1: Simple Start
1. **Double-click `start_ui.bat`** in your file explorer
2. Choose "1" for Simple UI when prompted
3. Your web browser will open automatically

### Option 2: PowerShell Start
1. **Right-click `start_ui.ps1`** → "Run with PowerShell"
2. Choose "1" for Simple UI when prompted
3. Your web browser will open automatically

### Option 3: Manual Start
1. Open Command Prompt in this folder
2. Type: `streamlit run simple_ui.py`
3. Go to `http://localhost:8501` in your browser

## 📋 Using the Simple Interface

### Step 1: Check Your Data
- ✅ **Gaming operators**: 20 operators loaded
- ✅ **Affiliate sites**: 20 sites loaded
- Files are ready to use!

### Step 2: Choose Settings
- **Pages per website**: Start with 10 (recommended)
- **Scraping speed**: Use "Medium" (2 seconds between requests)
- **Result quality**: Try "Medium quality" to filter out noise

### Step 3: Run the Scraper
- Click the big "🚀 START SCRAPING" button
- Watch the progress bar
- Results will be saved automatically

## 📊 Understanding Results

Your results will be saved in the `output/` folder as CSV files. Each result shows:

- **Operator Name**: Which gaming operator was found
- **Affiliate Site**: Which website mentioned it
- **Score**: How relevant the mention is (0-100)
- **URL**: The exact page where it was found
- **Context**: The text around the mention

### Quality Scores
- **0-29**: Low quality (might be false positive)
- **30-49**: Medium quality (probably relevant)
- **50-100**: High quality (very likely relevant)

## 💡 Tips for Best Results

1. **Start Small**: Begin with 5-10 pages per site to test
2. **Be Patient**: The tool waits between requests to be respectful
3. **Check High Scores**: Focus on results with scores above 50
4. **Regular Updates**: Keep your data files updated

## 🔧 Current Setup

- **Python Environment**: ✅ Virtual environment configured
- **Required Packages**: ✅ All installed (requests, beautifulsoup4, pandas, streamlit)
- **Data Files**: ✅ 20 operators and 20 sites loaded
- **Output Directory**: ✅ Ready for results

## 📁 Important Files

- **`start_ui.bat`** - Double-click this to start
- **`data/egaming_operators.csv`** - Your list of gaming operators
- **`data/affiliate_sites.csv`** - Your list of affiliate sites to search
- **`output/`** - Where results are saved

## 🆘 If You Need Help

### Common Issues:
- **"Browser doesn't open"**: Go to `http://localhost:8501` manually
- **"No results found"**: Try reducing the quality score or checking different sites
- **"Slow performance"**: Increase the delay between requests

### For Technical Issues:
1. Run `test_setup.py` to check if everything is working
2. Check that your CSV files have the correct format
3. Contact your technical team with specific error messages

## 🎯 You're All Set!

Everything is configured and ready to go. Double-click `start_ui.bat` to get started!

---

**Last tested**: July 18, 2025
**Status**: ✅ All systems working correctly
