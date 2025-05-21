# Social Media Sentiment Analysis

Social Media Sentiment Analysis is a lightweight, extensible content monitoring data pipeline that scans Reddit posts based on user-defined keywords—extracting, storing, and structuring the data for downstream analysis.

This project serves as a proof of concept (POC) for a broader content intelligence service designed to:

- Extend to Twitter and other platforms via public APIs
- Incorporate AI/ML models to flag harmful posts (e.g., misinformation, deepfakes, hate speech)
- Power dashboards or alerts for moderators, researchers, or social good initiatives

## Features

- Streamlit web app for interactive keyword search
- Uses the Reddit API via PRAW
- Loads credentials from a `.env` file
- Saves results to `data/reddit_results3.csv` and allows CSV download

## Setup

1. Clone the repository.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory with your Reddit API credentials:
   ```
   REDDIT_CLIENT_ID=your_client_id
   REDDIT_CLIENT_SECRET=your_client_secret
   REDDIT_USER_AGENT=your_user_agent
   ```
4. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

## Output

- Results are displayed in the web app and can be downloaded as a CSV.
- Results are also saved in `data/reddit_results3.csv` with columns: `Post ID`, `Title`, `Subreddit`, `Author`, `Created Time`, `Keyword Matched`, `Post URL`.

## Sample Output

| Post ID  | Title                        | Subreddit     | Author               | Created Time        | Keyword Matched | Post URL                                 |
|----------|------------------------------|---------------|----------------------|---------------------|-----------------|-------------------------------------------|
| 1krc58l  | $250/mo GoogleAI Ultra - Most expensive plan in AI industry! | DeepSeek      | BidHot8598           | 2025-05-20 18:21:27 | googleai        | https://i.redd.it/nwstw9dibz1f1.jpeg     |
| 1krc7tn  | Google da new 🍎 ‽ $250/mo GoogleAI Ultra - Most expensive plan in AI industry! | google        | BidHot8598           | 2025-05-20 18:24:21 | googleai        | https://i.redd.it/erc0p7w0cz1f1.jpeg     |
| 1kk69by  | Greek GoogleAi Translate      | GREEK         | statunknown          | 2025-05-11 17:24:06 | googleai        | https://www.reddit.com/gallery/1kk69by    |
| 1k9d7ub  | GoogleAI remains undefeated   | hockeymemes   | MurrayInBocaRaton    | 2025-04-27 20:10:17 | googleai        | https://i.redd.it/2x2uy8dzpfxe1.jpeg     |
| 1kghrzp  | Requesting r/googleai         | redditrequest | Individual-Spare-399 | 2025-05-06 22:32:29 | googleai        | https://reddit.com/r/googleai/            |

          

[ View the full CSV file](data/reddit_results3.csv)


