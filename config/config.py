import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_URL = os.getenv("API_BASE_URL")
    
    TIMEOUT = int(os.getenv("API_TIMEOUT", 10))

    EMAIL = os.getenv("API_EMAIL")

    PASSWORD = os.getenv("API_PASSWORD")

    API_KEY = os.getenv("API_KEY")