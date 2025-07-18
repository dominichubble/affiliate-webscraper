#!/usr/bin/env python3
"""
E-Gaming Affiliate Scraper - Simple Web UI
A user-friendly web interface for non-technical users to run the scraper
"""

import streamlit as st
import pandas as pd
import os
import sys
import json
from datetime import datetime
import time
import io

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from egaming_affiliate_scraper import EGamingAffiliateScraper

# Page configuration
st.set_page_config(
    page_title="E-Gaming Affiliate Scraper",
    page_icon="🎰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .stApp {
        background-color: #f0f2f6;
    }
    .main-header {
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
    }
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .error-box {
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .info-box {
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        color: #0c5460;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🎰 E-Gaming Affiliate Scraper</h1>
        <p>Find gaming operators mentioned on affiliate websites</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar configuration
    st.sidebar.header("⚙️ Configuration")
    
    # File upload section
    st.sidebar.subheader("📁 Upload Data Files")
    
    operators_file = st.sidebar.file_uploader(
        "Upload Operators CSV",
        type=['csv'],
        help="CSV file with columns: name, website, license, country"
    )
    
    sites_file = st.sidebar.file_uploader(
        "Upload Affiliate Sites CSV",
        type=['csv'],
        help="CSV file with columns: name, url, category, priority"
    )
    
    # Scraping parameters
    st.sidebar.subheader("🔧 Scraping Settings")
    
    max_pages = st.sidebar.slider(
        "Max pages per site",
        min_value=1,
        max_value=50,
        value=10,
        help="Maximum number of pages to scrape from each affiliate site"
    )
    
    delay = st.sidebar.slider(
        "Delay between requests (seconds)",
        min_value=1.0,
        max_value=10.0,
        value=2.0,
        step=0.5,
        help="Delay between requests to be respectful to websites"
    )
    
    min_score = st.sidebar.slider(
        "Minimum relevance score",
        min_value=0,
        max_value=100,
        value=30,
        help="Minimum e-gaming relevance score to include in results"
    )
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("📊 Data Preview")
        
        # Check for existing data files
        data_dir = os.path.join(os.path.dirname(__file__), 'data')
        default_operators = os.path.join(data_dir, 'egaming_operators.csv')
        default_sites = os.path.join(data_dir, 'affiliate_sites.csv')
        
        # Handle operators data
        if operators_file:
            try:
                operators_df = pd.read_csv(operators_file)
                st.success(f"✅ Operators file uploaded: {len(operators_df)} operators")
                st.dataframe(operators_df.head(), use_container_width=True)
            except Exception as e:
                st.error(f"❌ Error reading operators file: {e}")
                operators_df = None
        elif os.path.exists(default_operators):
            operators_df = pd.read_csv(default_operators)
            st.info(f"ℹ️ Using default operators file: {len(operators_df)} operators")
            st.dataframe(operators_df.head(), use_container_width=True)
        else:
            st.warning("⚠️ No operators file found. Please upload one.")
            operators_df = None
        
        # Handle sites data
        if sites_file:
            try:
                sites_df = pd.read_csv(sites_file)
                st.success(f"✅ Sites file uploaded: {len(sites_df)} sites")
                st.dataframe(sites_df.head(), use_container_width=True)
            except Exception as e:
                st.error(f"❌ Error reading sites file: {e}")
                sites_df = None
        elif os.path.exists(default_sites):
            sites_df = pd.read_csv(default_sites)
            st.info(f"ℹ️ Using default sites file: {len(sites_df)} sites")
            st.dataframe(sites_df.head(), use_container_width=True)
        else:
            st.warning("⚠️ No sites file found. Please upload one.")
            sites_df = None
    
    with col2:
        st.header("🚀 Run Scraper")
        
        # Status indicators
        if operators_df is not None and sites_df is not None:
            st.markdown("""
            <div class="success-box">
                <strong>✅ Ready to scrape!</strong><br>
                All required files are loaded.
            </div>
            """, unsafe_allow_html=True)
            
            # Estimated time calculation
            total_sites = len(sites_df)
            estimated_time = total_sites * max_pages * delay / 60  # in minutes
            st.info(f"⏱️ Estimated time: {estimated_time:.1f} minutes")
            
            # Run button
            if st.button("🎯 Start Scraping", type="primary", use_container_width=True):
                run_scraper(operators_df, sites_df, max_pages, delay, min_score)
        else:
            st.markdown("""
            <div class="error-box">
                <strong>❌ Cannot start scraping</strong><br>
                Please upload or ensure both CSV files are available.
            </div>
            """, unsafe_allow_html=True)
    
    # Recent results section
    st.header("📈 Recent Results")
    show_recent_results()

def run_scraper(operators_df, sites_df, max_pages, delay, min_score):
    """Run the scraper with the given parameters"""
    
    # Create progress indicators
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    try:
        # Initialize scraper
        status_text.text("🔧 Initializing scraper...")
        scraper = EGamingAffiliateScraper(max_pages_per_site=max_pages, delay=delay)
        
        # Save uploaded files temporarily and load them
        with st.spinner("📁 Loading data files..."):
            # Save operators data
            operators_file = "temp_operators.csv"
            operators_df.to_csv(operators_file, index=False)
            scraper.load_operators_from_csv(operators_file)
            
            # Save sites data
            sites_file = "temp_sites.csv"
            sites_df.to_csv(sites_file, index=False)
            scraper.load_affiliate_sites_from_csv(sites_file)
            
            # Clean up temp files
            os.remove(operators_file)
            os.remove(sites_file)
        
        progress_bar.progress(10)
        status_text.text(f"🌐 Starting to scrape {len(sites_df)} sites...")
        
        # Run scraping with progress updates
        all_matches = []
        total_sites = len(scraper.affiliate_sites)
        
        for i, site_info in enumerate(scraper.affiliate_sites):
            site_name = site_info.get('name', 'Unknown')
            status_text.text(f"🔍 Scraping site {i+1}/{total_sites}: {site_name}")
            
            try:
                site_matches = scraper.scrape_affiliate_site(site_info)
                all_matches.extend(site_matches)
                
                # Update progress
                progress = 10 + (i + 1) / total_sites * 80
                progress_bar.progress(int(progress))
                
            except Exception as e:
                st.warning(f"⚠️ Error scraping {site_name}: {str(e)}")
                continue
        
        status_text.text("🔄 Processing results...")
        progress_bar.progress(95)
        
        # Filter by minimum score
        if min_score > 0:
            original_count = len(all_matches)
            all_matches = [m for m in all_matches if m.get('egaming_score', 0) >= min_score]
            st.info(f"🎯 Filtered results: {len(all_matches)}/{original_count} matches above score {min_score}")
        
        # Save results
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = os.path.join(os.path.dirname(__file__), 'output')
        os.makedirs(output_dir, exist_ok=True)
        
        # Save CSV
        output_file = os.path.join(output_dir, f"egaming_findings_{timestamp}.csv")
        scraper.save_results_to_csv(all_matches, output_file)
        
        # Save summary
        summary = scraper.generate_summary_report(all_matches)
        summary_file = os.path.join(output_dir, f"egaming_summary_{timestamp}.json")
        with open(summary_file, 'w') as f:
            json.dump(summary, f, indent=2)
        
        progress_bar.progress(100)
        status_text.text("✅ Scraping completed successfully!")
        
        # Show results
        st.success("🎉 Scraping completed successfully!")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Matches", summary['total_matches'])
        with col2:
            st.metric("Unique Operators", summary['unique_operators_found'])
        with col3:
            st.metric("High Confidence", summary['high_confidence_matches'])
        
        # Show top results
        if all_matches:
            st.subheader("📊 Top Results")
            results_df = pd.DataFrame(all_matches)
            st.dataframe(results_df[['operator_name', 'affiliate_site', 'egaming_score', 'url']].head(10))
            
            # Download buttons
            col1, col2 = st.columns(2)
            with col1:
                csv_data = results_df.to_csv(index=False)
                st.download_button(
                    label="📥 Download CSV Results",
                    data=csv_data,
                    file_name=f"egaming_findings_{timestamp}.csv",
                    mime="text/csv"
                )
            with col2:
                json_data = json.dumps(summary, indent=2)
                st.download_button(
                    label="📥 Download Summary JSON",
                    data=json_data,
                    file_name=f"egaming_summary_{timestamp}.json",
                    mime="application/json"
                )
        
        # Clear progress indicators
        progress_bar.empty()
        status_text.empty()
        
    except Exception as e:
        st.error(f"❌ Error during scraping: {str(e)}")
        progress_bar.empty()
        status_text.empty()

def show_recent_results():
    """Show recent scraping results"""
    output_dir = os.path.join(os.path.dirname(__file__), 'output')
    
    if not os.path.exists(output_dir):
        st.info("🔍 No previous results found.")
        return
    
    # Find recent CSV files
    csv_files = [f for f in os.listdir(output_dir) if f.startswith('egaming_findings_') and f.endswith('.csv')]
    
    if not csv_files:
        st.info("🔍 No previous results found.")
        return
    
    # Sort by date (newest first)
    csv_files.sort(reverse=True)
    
    # Show dropdown to select file
    selected_file = st.selectbox(
        "Select a previous result to view:",
        csv_files,
        format_func=lambda x: f"📊 {x.replace('egaming_findings_', '').replace('.csv', '')}"
    )
    
    if selected_file:
        file_path = os.path.join(output_dir, selected_file)
        try:
            df = pd.read_csv(file_path)
            
            # Show summary stats
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Total Matches", len(df))
            with col2:
                st.metric("Unique Operators", df['operator_name'].nunique())
            with col3:
                st.metric("Unique Sites", df['affiliate_site'].nunique())
            with col4:
                st.metric("Avg Score", f"{df['egaming_score'].mean():.1f}")
            
            # Show data
            st.dataframe(df, use_container_width=True)
            
            # Download button
            csv_data = df.to_csv(index=False)
            st.download_button(
                label="📥 Download This Result",
                data=csv_data,
                file_name=selected_file,
                mime="text/csv"
            )
            
        except Exception as e:
            st.error(f"❌ Error loading file: {e}")

if __name__ == "__main__":
    main()
