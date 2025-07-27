# reddit_client.py
import praw
import datetime
import re  # Add at the top of the file if not already present
import time

class RedditScraper:
    def __init__(self, client_id, client_secret, user_agent):
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )

    def search_posts(self, keywords, limit=50):
        posts = []
        query = " ".join(keywords)
        # Fetch more to increase chance of enough matches
        for submission in self.reddit.subreddit('all').search(query, limit=limit*20):
            text = (submission.title + " " + submission.selftext).lower()
            if all(re.search(rf'\b{re.escape(k.lower())}\b', text) for k in keywords):
                if ("reddit.com" in submission.url or "redd.it" in submission.url or "v.redd.it" in submission.url):
                    created_time = datetime.datetime.utcfromtimestamp(
                        float(submission.created_utc)
                    ).strftime('%Y-%m-%d %H:%M:%S')
                    posts.append({
                        "Post ID": submission.id,
                        "Title": submission.title,
                        "Subreddit": submission.subreddit.display_name,
                        "Author": str(submission.author),
                        "Created Time": created_time,
                        "Keyword Matched": ", ".join(keywords),
                        "Post URL": f"https://www.reddit.com{submission.permalink}"
                    })
                if len(posts) == limit:
                    break
        return posts

    def search_subreddits(self, keywords, limit=20):
        found_subreddits = []
        query = " ".join(keywords)
        for subreddit in self.reddit.subreddits.search(query, limit=limit*20):
            name_and_desc = (subreddit.display_name + " " + subreddit.title + " " + subreddit.public_description).lower()
            if all(re.search(rf'\b{re.escape(k.lower())}\b', name_and_desc) for k in keywords):
                found_subreddits.append({
                    "Subreddit Name": subreddit.display_name,
                    "Title": subreddit.title,
                    "Description": subreddit.public_description,
                    "Subscribers": subreddit.subscribers,
                    "URL": f"https://www.reddit.com/r/{subreddit.display_name}/"
                })
                if len(found_subreddits) == limit:
                    break
        return found_subreddits

def monitor_new_posts(scraper, keywords, limit=50, interval_minutes=30):
    seen_ids = set()
    print(f"Monitoring for new posts every {interval_minutes} minutes for keywords: {keywords}")
    while True:
        print(f"\nChecking for new posts at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        new_posts = scraper.search_posts(keywords, limit=limit)
        fresh_posts = []
        for post in new_posts:
            if post["Post ID"] not in seen_ids:
                fresh_posts.append(post)
                seen_ids.add(post["Post ID"])
        if fresh_posts:
            print(f"Found {len(fresh_posts)} new post(s):")
            for post in fresh_posts:
                print(f"- {post['Title']} ({post['Post URL']})")
            # Optionally: save_to_csv(fresh_posts, "new_posts.csv")
        else:
            print("No new posts found.")
        time.sleep(interval_minutes * 60)  # Wait before next check
