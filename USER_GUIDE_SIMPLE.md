# E-Gaming Affiliate Scraper - User Guide

## 🚀 Quick Start for Non-Technical Users

This application is designed to be easy to use, even if you're not familiar with programming. Just follow these simple steps:

### Step 1: First-Time Setup (Only needed once)

1. **Double-click** `EASY_SETUP.bat`
2. Wait for the setup to complete (may take 5-10 minutes)
3. If prompted to install Python, follow the on-screen instructions

### Step 2: Using the Application

1. **Double-click** `START_APPLICATION.bat`
2. A web browser will automatically open with the scraper interface
3. Use the web interface to configure and run your scraping tasks

### ⚠️ Important Notes

- **Keep the black command window open** while using the application
- Closing the command window will stop the application
- You only need to run setup once
- Make sure you have an internet connection for the initial setup

### 🆘 Troubleshooting

#### Problem: Python not found

**Solution:**

1. Install Python from https://python.org/downloads
2. **IMPORTANT**: Check "Add Python to PATH" during installation
3. Restart your computer
4. Run `EASY_SETUP.bat` again

#### Problem: Setup fails with network error

**Solution:**

- Check your internet connection
- If you're on a corporate network, contact IT about Python package downloads

#### Problem: Browser doesn't open automatically

**Solution:**

- Manually open your web browser
- Go to: `http://localhost:8501`

### 📁 Files You Need to Know About

- `EASY_SETUP.bat` - Run this once to set up the application
- `START_APPLICATION.bat` - Run this to start the application
- `data/affiliate_sites.csv` - List of website URLs to scrape (you can edit this)
- `data/egaming_operators.csv` - List of operator names to look for

### 📝 Editing Your Data Files

**To add more operators:** Open `data/egaming_operators.csv` in Excel or Notepad and add operator names, one per line:

```
name
Bet365
William Hill
Your New Operator
```

**To add more websites:** Open `data/affiliate_sites.csv` in Excel or Notepad and add website URLs, one per line:

```
url
https://www.casinoguide.com
https://www.yoursite.com
```

### 🔄 Updating the Application

If you receive an updated version:

1. Replace all files with the new version
2. Your data files will be preserved
3. No need to run setup again (unless instructed)

### 📞 Getting Help

If you encounter any issues:

1. Check this troubleshooting guide first
2. Contact your technical support team
3. Include any error messages you see
