# 🎰 E-Gaming Affiliate Scraper

A user-friendly tool to find gaming operators mentioned on affiliate websites.

## 🚀 Quick Start

### For Non-Technical Users
1. **Double-click `START_HERE.bat`** (recommended)
2. **Or double-click `start_ui.bat`** (alternative)
3. Web browser will open automatically
4. Follow the 3-step process in the interface

### For Technical Users
```bash
# Install dependencies
pip install -r requirements.txt

# Run the UI
streamlit run simple_ui.py

# Or run the CLI
python src/egaming_scraper_cli.py --help
```

## 📁 Project Structure

```
├── START_HERE.bat         # 🎯 RECOMMENDED - Double-click to launch UI
├── start_ui.bat           # Alternative launcher
├── simple_ui.py           # Web interface
├── data/                  # Your input CSV files
│   ├── egaming_operators.csv
│   └── affiliate_sites.csv
├── output/                # Results are saved here
├── src/                   # Core scraper code
└── docs/                  # Documentation
```

## 📋 How It Works

1. **Upload/Check Data**: Gaming operators and affiliate sites from CSV files
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

## 💡 Tips

- Start with 5-10 pages per site for testing
- Use "Medium" speed (2 seconds between requests)
- Focus on results with scores above 50
- Keep your CSV files updated

## 🔧 Requirements

- Python 3.8+
- Internet connection
- CSV files with operators and affiliate sites

## 📞 Support

1. Run `test_setup.py` to verify everything works
2. Check `docs/USER_GUIDE.md` for detailed instructions
3. See `docs/TECHNICAL.md` for advanced configuration
4. Contact technical support with specific error messages

---

**Ready to start?** Double-click `START_HERE.bat` 🚀
