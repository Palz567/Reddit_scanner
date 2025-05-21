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

    keyword = "deepfake"  
    print(f"Searching Reddit for posts containing: '{keyword}'...")
    results = scraper.search_posts(keyword)

    data_path = os.path.join(config["data_dir"], "reddit_results3.csv")
    save_to_csv(results, keyword, filename=data_path)

if __name__ == "__main__":
    main()
