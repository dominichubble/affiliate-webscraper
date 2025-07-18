#!/usr/bin/env python3
"""
E-Gaming Affiliate Scraper - Simple UI
A beginner-friendly interface for the scraper
"""

import streamlit as st
import pandas as pd
import os
import sys
import json
from datetime import datetime

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from egaming_affiliate_scraper import EGamingAffiliateScraper
except ImportError:
    st.error("❌ Could not import scraper. Please ensure all files are in the correct location.")
    st.stop()

# Page configuration
st.set_page_config(
    page_title="Gaming Scraper",
    page_icon="🎰",
    layout="wide"
)

# Simple styling
st.markdown("""
<style>
.big-font {
    font-size: 24px !important;
    font-weight: bold;
    color: #1f4e79;
}
.success-message {
    background-color: #d4edda;
    color: #155724;
    padding: 15px;
    border-radius: 5px;
    margin: 10px 0;
}
.error-message {
    background-color: #f8d7da;
    color: #721c24;
    padding: 15px;
    border-radius: 5px;
    margin: 10px 0;
}
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown('<p class="big-font">🎰 Gaming Operator Finder</p>', unsafe_allow_html=True)
    st.markdown("**Find gaming operators mentioned on affiliate websites**")
    
    # Simple 3-step process
    st.markdown("---")
    
    # Step 1: Check data files
    st.subheader("Step 1: Check Your Data Files")
    
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    operators_file = os.path.join(data_dir, 'egaming_operators.csv')
    sites_file = os.path.join(data_dir, 'affiliate_sites.csv')
    
    operators_exists = os.path.exists(operators_file)
    sites_exists = os.path.exists(sites_file)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if operators_exists:
            st.success("✅ Gaming operators file found")
            try:
                ops_df = pd.read_csv(operators_file)
                st.write(f"📊 {len(ops_df)} operators loaded")
            except:
                st.error("❌ Error reading operators file")
                ops_df = None
        else:
            st.error("❌ Gaming operators file missing")
            st.write("Please add: `data/egaming_operators.csv`")
            ops_df = None
    
    with col2:
        if sites_exists:
            st.success("✅ Affiliate sites file found")
            try:
                sites_df = pd.read_csv(sites_file)
                st.write(f"🌐 {len(sites_df)} sites loaded")
            except:
                st.error("❌ Error reading sites file")
                sites_df = None
        else:
            st.error("❌ Affiliate sites file missing")
            st.write("Please add: `data/affiliate_sites.csv`")
            sites_df = None
    
    # Step 2: Settings
    st.subheader("Step 2: Choose Your Settings")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        pages = st.selectbox(
            "Pages per website:",
            [5, 10, 15, 20, 25],
            index=1,
            help="How many pages to check on each website"
        )
    
    with col2:
        speed = st.selectbox(
            "Scraping speed:",
            ["Slow (3 sec)", "Medium (2 sec)", "Fast (1 sec)"],
            index=1,
            help="How fast to scrape (slower is more respectful)"
        )
        delay = {"Slow (3 sec)": 3.0, "Medium (2 sec)": 2.0, "Fast (1 sec)": 1.0}[speed]
    
    with col3:
        quality = st.selectbox(
            "Result quality:",
            ["Show all results", "Medium quality (30+)", "High quality (50+)"],
            index=1,
            help="What quality of results to show"
        )
        min_score = {"Show all results": 0, "Medium quality (30+)": 30, "High quality (50+)": 50}[quality]
    
    # Step 3: Run scraper
    st.subheader("Step 3: Run the Scraper")
    
    if operators_exists and sites_exists and ops_df is not None and sites_df is not None:
        # Show summary
        st.info(f"📋 Ready to search {len(ops_df)} operators across {len(sites_df)} websites")
        
        # Estimate time
        estimated_minutes = len(sites_df) * pages * delay / 60
        st.write(f"⏱️ Estimated time: {estimated_minutes:.1f} minutes")
        
        # Big start button
        if st.button("🚀 START SCRAPING", type="primary", use_container_width=True):
            run_simple_scraper(ops_df, sites_df, pages, delay, min_score)
    else:
        st.error("❌ Cannot start - please check your data files above")
    
    # Show recent results
    st.markdown("---")
    st.subheader("📊 Previous Results")
    show_simple_results()

def run_simple_scraper(ops_df, sites_df, pages, delay, min_score):
    """Run the scraper with simplified interface"""
    
    # Create containers for updates
    status_container = st.empty()
    progress_container = st.empty()
    results_container = st.empty()
    
    try:
        # Initialize
        status_container.info("🔧 Setting up scraper...")
        scraper = EGamingAffiliateScraper(max_pages_per_site=pages, delay=delay)
        
        # Load data temporarily
        temp_ops = "temp_operators.csv"
        temp_sites = "temp_sites.csv"
        
        ops_df.to_csv(temp_ops, index=False)
        sites_df.to_csv(temp_sites, index=False)
        
        scraper.load_operators_from_csv(temp_ops)
        scraper.load_affiliate_sites_from_csv(temp_sites)
        
        # Clean up
        os.remove(temp_ops)
        os.remove(temp_sites)
        
        # Progress tracking
        total_sites = len(sites_df)
        all_matches = []
        
        # Create progress bar
        progress = progress_container.progress(0)
        
        # Scrape each site
        for i, site_info in enumerate(scraper.affiliate_sites):
            site_name = site_info.get('name', 'Unknown')[:30]  # Truncate long names
            
            # Update status
            status_container.info(f"🔍 Checking website {i+1}/{total_sites}: {site_name}")
            
            try:
                matches = scraper.scrape_affiliate_site(site_info)
                all_matches.extend(matches)
                
                # Update progress
                progress.progress((i + 1) / total_sites)
                
            except Exception as e:
                st.warning(f"⚠️ Skipped {site_name}: {str(e)[:50]}")
                continue
        
        # Filter results
        if min_score > 0:
            original_count = len(all_matches)
            all_matches = [m for m in all_matches if m.get('egaming_score', 0) >= min_score]
            status_container.success(f"✅ Found {len(all_matches)} quality matches (filtered from {original_count})")
        else:
            status_container.success(f"✅ Found {len(all_matches)} total matches")
        
        # Save results
        if all_matches:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_dir = os.path.join(os.path.dirname(__file__), 'output')
            os.makedirs(output_dir, exist_ok=True)
            
            # Save files
            csv_file = os.path.join(output_dir, f"egaming_findings_{timestamp}.csv")
            scraper.save_results_to_csv(all_matches, csv_file)
            
            # Show results summary
            with results_container.container():
                st.markdown('<div class="success-message">🎉 <strong>Scraping Completed Successfully!</strong></div>', unsafe_allow_html=True)
                
                # Summary stats
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Total Matches", len(all_matches))
                with col2:
                    operators_found = len(set(m['operator_name'] for m in all_matches))
                    st.metric("Operators Found", operators_found)
                with col3:
                    high_quality = len([m for m in all_matches if m.get('egaming_score', 0) >= 50])
                    st.metric("High Quality", high_quality)
                
                # Show sample results
                df = pd.DataFrame(all_matches)
                st.write("**Top 10 Results:**")
                sample_df = df[['operator_name', 'affiliate_site', 'egaming_score']].head(10)
                st.dataframe(sample_df, use_container_width=True)
                
                # Download button
                csv_data = df.to_csv(index=False)
                st.download_button(
                    label="📥 Download Full Results (CSV)",
                    data=csv_data,
                    file_name=f"gaming_results_{timestamp}.csv",
                    mime="text/csv",
                    use_container_width=True
                )
        else:
            results_container.warning("😔 No matches found. Try adjusting your settings or checking your data files.")
        
        # Clear progress
        progress_container.empty()
        
    except Exception as e:
        status_container.error(f"❌ Error: {str(e)}")
        progress_container.empty()

def show_simple_results():
    """Show previous results in a simple format"""
    output_dir = os.path.join(os.path.dirname(__file__), 'output')
    
    if not os.path.exists(output_dir):
        st.info("No previous results found.")
        return
    
    # Find CSV files
    csv_files = [f for f in os.listdir(output_dir) if f.endswith('.csv') and 'egaming_findings_' in f]
    
    if not csv_files:
        st.info("No previous results found.")
        return
    
    # Sort by date (newest first)
    csv_files.sort(reverse=True)
    
    # Show only the most recent 5 files
    for i, filename in enumerate(csv_files[:5]):
        file_path = os.path.join(output_dir, filename)
        
        # Extract date from filename
        try:
            date_part = filename.replace('egaming_findings_', '').replace('.csv', '')
            date_formatted = datetime.strptime(date_part, '%Y%m%d_%H%M%S').strftime('%Y-%m-%d %H:%M')
        except:
            date_formatted = date_part
        
        with st.expander(f"📊 Results from {date_formatted}"):
            try:
                df = pd.read_csv(file_path)
                
                # Quick stats
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Matches", len(df))
                with col2:
                    st.metric("Operators", df['operator_name'].nunique())
                with col3:
                    st.metric("High Quality", len(df[df['egaming_score'] >= 50]))
                
                # Sample data
                if len(df) > 0:
                    st.write("**Sample Results:**")
                    sample = df[['operator_name', 'affiliate_site', 'egaming_score']].head(5)
                    st.dataframe(sample, use_container_width=True)
                
                # Download button
                csv_data = df.to_csv(index=False)
                st.download_button(
                    label="📥 Download",
                    data=csv_data,
                    file_name=filename,
                    mime="text/csv",
                    key=f"download_{i}"
                )
                
            except Exception as e:
                st.error(f"Error loading file: {e}")

if __name__ == "__main__":
    main()
