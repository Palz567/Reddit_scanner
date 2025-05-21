# utils.py
import pandas as pd
import os

def save_to_csv(posts, filename):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df = pd.DataFrame(posts, columns=["Post ID", "Title", "Subreddit", "Author", "Created Time", "Keyword Matched", "Post URL"])
    if os.path.exists(filename):
        df.to_csv(filename, mode='a', header=False, index=False)
    else:
        df.to_csv(filename, index=False)
    print(f"Saved {len(posts)} posts to {filename}")