from fastapi import Header, HttpException
from app.core.config import settings
from app.core.security import verify_token

# Checking the API key correctness
def get_api_key(api_key: str = Header(...)):
    if api_key != settings.API_KEY:
        raise HttpException(status_code=403,detail='Invalid API Key')

# Get the current user details from input token
def get_current_user(token: str = Header(...)):
    payload = verify_token(token)
    if not payload:
        raise HttpException(status_code = 401,detail = 'Invalid JWT token')
    return payload