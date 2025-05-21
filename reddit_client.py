# scraper.py
import praw
import datetime

class RedditScraper:
    def __init__(self, client_id, client_secret, user_agent):
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )

    def search_posts(self, keyword, limit=50):
        posts = []
        for submission in self.reddit.subreddit('all').search(keyword, limit=limit):
            if keyword.lower() in submission.title.lower() or keyword.lower() in submission.selftext.lower():
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
                        "Keyword Matched": keyword,
                        "Post URL": submission.url
                    })
        return posts
