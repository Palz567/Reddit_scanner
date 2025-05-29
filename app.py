import streamlit as st
from reddit_client import RedditScraper
from utils import save_to_csv
from config import load_config
import os
import pandas as pd
import logging  # import for logging

logging.basicConfig(
    filename='project_kavach.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)   #logging configuration

# Load Reddit API configuration
config = load_config()
logging.info("Reddit API configuration loaded.") # logg file

# Initialize scraper
scraper = RedditScraper(
    config["client_id"],
    config["client_secret"],
    config["user_agent"]
)
logging.info("RedditScraper initialized.") # logg file

st.title("Project Kavach")

# UI for user input
keywords_input = st.text_input("Enter keyword(s) to search on Reddit (comma-separated):", value="Financial Fraud,AI Fraud,Deepfake")
keywords = [k.strip() for k in keywords_input.split(",") if k.strip()]
limit = st.number_input("Number of results (Last 1 Year)", min_value=1, max_value=10000, value=20, step=1)


if st.button("Search"):
    logging.info(f"User initiated search for keywords: {keywords} with limit: {limit}")  #logg file 

    with st.spinner(f"Searching Reddit for: {', '.join(keywords)}"):
        all_results = []
        for keyword in keywords:
            logging.info(f"Searching posts for keyword: {keyword}") # logg file 
            results = scraper.search_posts(keyword, limit=limit)
            all_results.extend(results)
            logging.info(f"Found {len(results)} posts for keyword: {keyword}") # logg file 

        if all_results:
            logging.info(f"Total posts found: {len(all_results)}") #logg file 
            st.success(f"Found {len(all_results)} posts for '{', '.join(keywords)}'.")
            # Show results in a table
            df = pd.DataFrame(all_results, columns=[
                "Post ID", "Title", "Subreddit", "Author", "Created Time", "Keyword Matched", "Post URL"
            ])
            st.dataframe(df)
            logging.info("Results displayed in UI and CSV download offered.") #logg file 

            # Option to download as CSV
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download results as CSV",
                data=csv,
                file_name=f"reddit_{'_'.join(keywords)}_results.csv",
                mime="text/csv"
            )

            # Also save to data directory
            data_path = os.path.join(config["data_dir"], "reddit_results3.csv")
            save_to_csv(all_results, filename=data_path)
            logging.info(f"Results saved to {data_path}") #logg file 
        else:
            st.warning("No posts found for these keywords.")
            logging.info("No posts found for these keywords.") #logg file
        
