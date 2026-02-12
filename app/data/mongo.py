from pathlib import Path
import os

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi

ENV_PATH = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path=ENV_PATH)

DB_URI = os.getenv("DB_URI")
DB_NAME = os.getenv("DB_NAME", "students_db")

if not DB_URI:
    raise ValueError(f"DB_URI is missing. Set it in {ENV_PATH}")

# Keep client creation lightweight at import time.
# PyMongo connects lazily; operations will fail later if URI/cluster is invalid.
client = MongoClient(DB_URI, server_api=ServerApi("1"))
db = client[DB_NAME]


def get_collection(name: str):
    return db[name]
