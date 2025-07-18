#!/usr/bin/env python3
"""
Test script to verify the scraper and UI setup works correctly
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_imports():
    """Test that all required packages can be imported"""
    try:
        print("Testing imports...")
        
        # Test core packages
        import requests
        print("✓ requests imported successfully")
        
        import bs4
        print("✓ BeautifulSoup4 imported successfully")
        
        import pandas as pd
        print("✓ pandas imported successfully")
        
        import streamlit as st
        print("✓ streamlit imported successfully")
        
        # Test our scraper
        from egaming_affiliate_scraper import EGamingAffiliateScraper
        print("✓ EGamingAffiliateScraper imported successfully")
        
        # Test that scraper can be instantiated
        scraper = EGamingAffiliateScraper(max_pages_per_site=1, delay=1.0)
        print("✓ EGamingAffiliateScraper instantiated successfully")
        
        print("\n🎉 All imports successful! The scraper is ready to use.")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def test_data_files():
    """Test that data files exist and are readable"""
    print("\nTesting data files...")
    
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    operators_file = os.path.join(data_dir, 'egaming_operators.csv')
    sites_file = os.path.join(data_dir, 'affiliate_sites.csv')
    
    if os.path.exists(operators_file):
        print("✓ egaming_operators.csv found")
        try:
            import pandas as pd
            df = pd.read_csv(operators_file)
            print(f"  - {len(df)} operators loaded")
        except Exception as e:
            print(f"  - ❌ Error reading operators file: {e}")
    else:
        print("⚠️  egaming_operators.csv not found")
        print("   Please create this file in the data/ directory")
    
    if os.path.exists(sites_file):
        print("✓ affiliate_sites.csv found")
        try:
            import pandas as pd
            df = pd.read_csv(sites_file)
            print(f"  - {len(df)} sites loaded")
        except Exception as e:
            print(f"  - ❌ Error reading sites file: {e}")
    else:
        print("⚠️  affiliate_sites.csv not found")
        print("   Please create this file in the data/ directory")

def test_output_directory():
    """Test that output directory exists or can be created"""
    print("\nTesting output directory...")
    
    output_dir = os.path.join(os.path.dirname(__file__), 'output')
    
    if os.path.exists(output_dir):
        print("✓ output directory exists")
    else:
        try:
            os.makedirs(output_dir, exist_ok=True)
            print("✓ output directory created")
        except Exception as e:
            print(f"❌ Error creating output directory: {e}")

def main():
    """Run all tests"""
    print("E-Gaming Affiliate Scraper - Setup Test")
    print("=" * 50)
    
    # Test imports
    if not test_imports():
        print("\n❌ Setup failed - imports not working")
        return False
    
    # Test data files
    test_data_files()
    
    # Test output directory
    test_output_directory()
    
    print("\n" + "=" * 50)
    print("🎯 Setup test completed!")
    print("\nTo start the UI:")
    print("  - Double-click start_ui.bat")
    print("  - Or run: streamlit run simple_ui.py")
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)
