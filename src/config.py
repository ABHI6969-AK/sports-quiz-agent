import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

CHROMA_DB_PATH = "chroma_db"
SPORTS_DATA_PATH = "data/sports_facts.json"

MODEL_NAME = "llama-3.3-70b-versatile"

DEFAULT_NUM_QUESTIONS = 5