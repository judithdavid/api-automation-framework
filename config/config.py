import os

class Config:
    BASE_URL = os.getenv(
        "API_BASE_URL",
        "https://jsonplaceholder.typicode.com"
    )
