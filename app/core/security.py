from app.core.config import settings
from datetime import datetime,timezone,timedelta
from jose import jwt,JWTError


# Creating a JWT token
def create_token(data: dict,expire_minutes=30):
    to_encode = data.copy()
    expire_time = datetime.now(timezone.utc) + timedelta(minutes = expire_minutes)
    to_encode.update({'exp':expire_time})
    return jwt.encode(
        to_encode,  settings.JWT_SECRET_KEY, algorithm = settings.JWT_ALGORITHM
    )

# Verifying the JWT token
def verify_token(token:str):
    try:
        payload = jwt.decode(
            token, settings.JWT_SECRET_KEY,algorithms=[settings.JWT_ALGORITHM]
        )
        return payload
    except JWTError:
        return None
