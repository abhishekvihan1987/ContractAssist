import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GCS_KEY_PATH = os.getenv("GCS_KEY_PATH")
    PROJECT_ID = os.getenv("PROJECT_ID")
    LOCATION = os.getenv("LOCATION")

settings = Settings()