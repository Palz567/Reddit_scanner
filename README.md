
# Project Kavach

### AI-powered Reddit Intelligence for Ethical Social Impact

**Project Kavach** is a modular, next-gen public discourse analysis system engineered to support the core mission of [Project Karna](https://www.projectkarna.com/): safeguarding digital dignity, combating misinformation, and strengthening civic awareness.

This platform transforms Reddit's raw conversation threads into structured, ethically sourced insights—ready to power research, policy dashboards, and AI/LLM pipelines.

---

##  Why This Project Matters

Project Kavach is dedicated to promoting a safe, inclusive, and ethical digital space. Project Kavach contributes by:

-  Context-aware monitoring of misinformation and hate speech
-  On-demand Reddit trend analysis
-  AI-ready backend for NLP pipelines
-  Ethical, reproducible data collection for researchers & NGOs

---

## Features

-  **Multi-keyword search** (matches posts containing any of the keywords)
-  **On-demand Reddit data scraping** using PRAW
-  **Structured CSV export** with metadata
-  **Streamlit UI** for search & visualization
-  **Secure API key management** using `.env`
-  **Modular ML/NLP integration** for future sentiment analysis or misinformation flagging

---

##  Quick Start
1. **Clone the repository:**

```bash
git clone https://github.com/Palz567/Reddit_scanner.git
cd Reddit_scanner
pip install -r requirements.txt
```

Create a `.env` file:

```env
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=your_user_agent
```

Run the Streamlit app:

```bash
streamlit run app.py
```

---
## Output

- Results are displayed in the web app and can be downloaded as a CSV.
- Results are also saved in `data/reddit_results3.csv` with columns: `Post ID`, `Title`, `Subreddit`, `Author`, `Created Time`, `Keyword Matched`, `Post URL`.

## Sample Output Table

| Post ID   | Title                                         | Subreddit           | Author               | Created Time        | Keyword Matched | Post URL                                                                                   |
|-----------|-----------------------------------------------|---------------------|----------------------|---------------------|-----------------|--------------------------------------------------------------------------------------------|
| 1kk69by   | Greek GoogleAi Translate                      | GREEK               | statunknown          | 11-05-2025 17:24    | googleai        | https://www.reddit.com/r/GREEK/comments/1kk69by/greek_googleai_translate/                                              |                                                   |
| 1kg9ptd   | Deepfakes are getting insane                  | ThatsInsane         | PradipJayakumar      | 06-05-2025 17:02    | deepfake        | https://www.reddit.com/r/ThatsInsane/comments/1kg9ptd/deepfakes_are_getting_insane/                                                    |                                            |
| 1is0rg6   | I am so confused. Is this AI, deepfake, or both? Why does it look so good? | Corridor | SiebelReddiT | 18-02-2025 01:24 | deepfake        | https://www.reddit.com/r/Corridor/comments/1is0rg6/i_am_so_confused_is_this_ai_deepfake_or_both_why/                                                    |
| 1bpy7s6   | Deepfake at its best                          | friends_tv_show     | Mad_Humor            | 28-03-2024 15:22    | deepfake        | https://www.reddit.com/r/friends_tv_show/comments/1bpy7s6/deepfake_at_its_best/                                                    |
| 1f31m5b   | Livestream deepfakes are happening            | Damnthatsinteresting| MetaKnowing          | 28-08-2024 04:38    | deepfake        | https://www.reddit.com/r/Damnthatsinteresting/comments/1f31m5b/livestream_deepfakes_are_happening/                                                    |
| 1ijpq5e   | The RBI is set to introduce the ‘.bank.in’ domain for Indian banks to tackle financial fraud....!! | IndianStreetBets | Just_Chill_Yaar | 2025-02-07 07:40:14 | Financial Fraud    | https://www.reddit.com/r/IndianStreetBets/comments/1ijpq5e/the_rbi_is_set_to_introduce_the_bankin_domain_for/ |

[View the full CSV file](data/reddit_results3.csv)



---

##  Future Enhancements

- **Advanced filtering:** Implement multi-keyword AND logic and date range filtering
- **Broaden platform support:** Integrate data sources like Twitter, YouTube, and more
- **Enhance sentiment analysis:** Implement advanced NLP models for deeper insights
- **Develop alerting mechanisms:** Notify users or moderators about critical trends or posts
- **Create comprehensive dashboards:** Visualize trends, sentiments, and key metrics over time

---





