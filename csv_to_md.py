import pandas as pd

df = pd.read_csv('data/reddit_results3.csv')
print(df.head(5).to_markdown(index=False))