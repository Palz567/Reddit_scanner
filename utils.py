# utils.py
import pandas as pd
import os

def save_to_csv(urls, keyword, filename):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df = pd.DataFrame(urls, columns=['Post URL'])
    df['Keyword'] = keyword
    if os.path.exists(filename):
        df.to_csv(filename, mode='a', header=False, index=False)
    else:
        df.to_csv(filename, index=False)
    print(f"Saved {len(urls)} URLs for keyword '{keyword}' to {filename}")
