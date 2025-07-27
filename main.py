# main.py
from config import load_config
from reddit_client import RedditScraper, monitor_new_posts
from utils import save_to_csv
import os

def main():
    config = load_config()

    scraper = RedditScraper(
        config["client_id"],
        config["client_secret"],
        config["user_agent"]
    )

    keywords = ["deepfake", "scam"]  # Your keywords here
    monitor_new_posts(scraper, keywords, limit=50, interval_minutes=30)

    print(f"Searching Reddit for posts containing ALL keywords: {keywords}...")
    results = scraper.search_posts(keywords, limit=50)
    all_results = results  # Only one search needed

    data_path = os.path.join(config["data_dir"], "reddit_results3.csv")
    save_to_csv(all_results, filename=data_path)

if __name__ == "__main__":
    main()
