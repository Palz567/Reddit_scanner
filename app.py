import streamlit as st
from reddit_client import RedditScraper
from utils import save_to_csv
from config import load_config
import os
import pandas as pd

# Load Reddit API configuration
config = load_config()

# Initialize scraper
scraper = RedditScraper(
    config["client_id"],
    config["client_secret"],
    config["user_agent"]
)

st.title("Social Media Sentiment Analysis")

# UI for user input
keyword = st.text_input("Enter keyword to search on Reddit:", value="deepfake")
limit = st.number_input("Number of results", min_value=1, max_value=100, value=20, step=1)

if st.button("Search"):
    with st.spinner(f"Searching Reddit for '{keyword}'..."):
        results = scraper.search_posts(keyword, limit=limit)
        if results:
            st.success(f"Found {len(results)} posts for '{keyword}'.")
            # Show results in a table
            df = pd.DataFrame(results, columns=[
                "Post ID", "Title", "Subreddit", "Author", "Created Time", "Keyword Matched", "Post URL"
            ])
            st.dataframe(df)

            # Option to download as CSV
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download results as CSV",
                data=csv,
                file_name=f"reddit_{keyword}_results.csv",
                mime="text/csv"
            )

            # Also save to data directory
            data_path = os.path.join(config["data_dir"], "reddit_results3.csv")
            save_to_csv(results, filename=data_path)
        else:
            st.warning("No posts found for this keyword.")
