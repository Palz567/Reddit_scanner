# reddit_client.py
import praw
import datetime
import re  # Add at the top of the file if not already present

class RedditScraper:
    def __init__(self, client_id, client_secret, user_agent):
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )

    def search_posts(self, keywords, limit=50):
        posts = []
        # Join keywords for a single search query (Reddit search supports this)
        query = " ".join(keywords)
        for submission in self.reddit.subreddit('all').search(query, limit=limit*2):  # fetch more to ensure enough matches
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
