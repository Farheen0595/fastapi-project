import os
from dotenv import load_dotenv  

load_dotenv() # Load environment variables from .env file




class Settings:

    PROJECT_NAME = "Car Price API"
    API_KEY = os.getenv("API_KEY","demo-key")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY","secret123")
    REDIS_URL = os.getenv("REDIS_URL","redis://localhost:6379")
    JWT_ALGORITHM = "HS256"
    MODEL_PATH = "app/models/model.pkl"


settings = Settings()