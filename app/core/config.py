import os
from dotenv import load_dotenv

# Loads the .env file contents
load_dotenv()

# Setting all the global configurations of the application
class Settings:
    API_KEY = os.getenv('API_KEY','demo-key')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY','secret')
    REDIS_URL = os.getenv('REDIS_URL','redis://localhost:6379')
    JWT_ALGORITHM = 'HS256'
    MODEL_PATH = 'app/models/model.pkl'

# Creating an instance of the Settings class
settings = Settings()


