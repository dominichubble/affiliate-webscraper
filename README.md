# 🎰 E-Gaming Affiliate Scraper

A user-friendly tool to find gaming operators mentioned on affiliate websites.

## 🚀 Quick Start for Non-Technical Users

### Step 1: First-Time Setup (Run Once)

1. **Double-click `EASY_SETUP.bat`** - This installs everything automatically
2. Wait for setup to complete (5-10 minutes)
3. If prompted to install Python, follow the instructions

### Step 2: Using the Application

1. **Double-click `START_APPLICATION.bat`** - This starts the scraper
2. A web browser will open automatically with the interface
3. Keep the black window open while using the application

### ⚠️ Important Notes

- **Keep the command window open** while using the application
- Closing the command window will stop the application
- You only need to run setup once
- Make sure you have an internet connection for the initial setup

## 🔧 For Technical Users

### Quick Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Run the web UI
streamlit run simple_ui.py

# Or run from command line
python src/egaming_scraper_cli.py --help
```

## 📁 Project Structure

```
├── EASY_SETUP.bat         # 🔧 First-time setup (run once)
├── START_APPLICATION.bat  # 🎯 Start the application
├── simple_ui.py           # Web interface
├── test_setup.py          # Verify installation
├── requirements.txt       # Python dependencies
├── data/                  # Your input CSV files
│   ├── egaming_operators.csv
│   └── affiliate_sites.csv
├── output/                # Results are saved here
├── src/                   # Core scraper code
│   ├── egaming_affiliate_scraper.py
│   └── egaming_scraper_cli.py
└── docs/                  # Documentation
    ├── USER_GUIDE.md
    └── TECHNICAL.md
```

## 📋 How It Works

1. **Upload/Check Data**: Gaming operators (names only) and affiliate sites (URLs only) from simple CSV files
2. **Configure Settings**: Pages per site, speed, quality filters
3. **Run Scraper**: Automatically searches and finds mentions
4. **Download Results**: Get CSV files with all findings

## 📊 Results Format

Each result includes:

- **Operator Name**: Which gaming company was found
- **Affiliate Site**: Which website mentioned it
- **Relevance Score**: 0-100 (higher = more relevant)
- **URL**: Exact page where mentioned
- **Context**: Text snippet around the mention

## 💡 Tips for Best Results

- Start with 5-10 pages per site for testing
- Use "Medium" speed (2 seconds between requests)
- Focus on results with scores above 50
- Keep your CSV files updated

## 🆘 Troubleshooting

### Problem: Python not found

**Solution:**

1. Install Python from https://python.org/downloads
2. **IMPORTANT**: Check "Add Python to PATH" during installation
3. Restart your computer
4. Run `EASY_SETUP.bat` again

### Problem: Setup fails with network error

**Solution:**

- Check your internet connection
- If you're on a corporate network, contact IT about Python package downloads

### Problem: Browser doesn't open automatically

**Solution:**

- Manually open your web browser
- Go to: `http://localhost:8501`

## 🔧 Requirements

- Python 3.8+
- Internet connection
- Simple CSV files with operator names and affiliate site URLs

## 📞 Support

1. Run `test_setup.py` to verify everything works
2. Check `USER_GUIDE_SIMPLE.md` for detailed instructions
3. See `docs/USER_GUIDE.md` and `docs/TECHNICAL.md` for advanced configuration
4. Contact technical support with specific error messages

---

**Ready to start?**

- **Non-technical users**: Double-click `EASY_SETUP.bat` then `START_APPLICATION.bat`
- **Technical users**: Run `streamlit run simple_ui.py`
