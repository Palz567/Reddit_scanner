# config.py
import os
from dotenv import load_dotenv

def load_config():
    load_dotenv()
    config = {
        "client_id": os.getenv("REDDIT_CLIENT_ID"),
        "client_secret": os.getenv("REDDIT_CLIENT_SECRET"),
        "user_agent": os.getenv("REDDIT_USER_AGENT"),
        "data_dir": os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
    }
    return config
