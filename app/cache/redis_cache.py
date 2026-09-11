#import json
import os
import redis
#from app.core.config import settings
from dotenv import load_dotenv  # added for render deployment

load_dotenv()  # Load environment variables from .env file

REDIS_URL = os.getenv("REDIS_URL")  # Get the Redis URL from environment variables

#redis_client = redis.Redis.from_url(settings.REDIS_URL)

# Use the Redis URL from environment variables (added for render deployment)
redis_client = redis.StrictRedis.from_url(REDIS_URL, decode_responses=True)  

def get_cached_prediction(key: str):
    """
    Retrieve the cached prediction for the given input data from Redis.
    """
    value = redis_client.get(key)
    # if value:
    #     return json.loads(value)
    # return None

    return eval(value) if value else None  # Use eval to convert string back to dictionary

def set_cached_prediction(key: str, value: dict, expiry: int = 3600):
    #redis_client.setex(key, expiry, json.dumps(value))

    redis_client.set(key,str(value))