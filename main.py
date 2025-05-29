# main.py
from config import load_config
from reddit_client import RedditScraper
from utils import save_to_csv
import os

def main():
    config = load_config()

    scraper = RedditScraper(
        config["client_id"],
        config["client_secret"],
        config["user_agent"]
    )

    keywords = ["deepfake", "AI", "machine learning"]  # List your keywords here

    all_results = []
    for keyword in keywords:
        print(f"Searching Reddit for posts containing: '{keyword}'...")
        results = scraper.search_posts(keyword)
        all_results.extend(results)  # Collect all results

    data_path = os.path.join(config["data_dir"], "reddit_results3.csv")
    save_to_csv(all_results, filename=data_path)

if __name__ == "__main__":
    main()
