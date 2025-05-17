# Reddit Keyword Scraper

This project provides a web-based UI to search Reddit for posts containing a specified keyword and download the results as a CSV file.

## Features

- Streamlit web app for interactive keyword search
- Uses the Reddit API via PRAW
- Loads credentials from a `.env` file
- Saves results to `data/reddit_results2.csv` and allows CSV download

## Setup

1. Clone the repository.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory with your Reddit API credentials:
   ```
   REDDIT_CLIENT_ID="your_client_id"
   REDDIT_CLIENT_SECRET="your_client_secret"
   REDDIT_USER_AGENT="your_user_agent"
   ```
4. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

## Output

- Results are displayed in the web app and can be downloaded as a CSV.
- Results are also saved in `data/reddit_results2.csv` with columns: `Post URL`, `Keyword`.
