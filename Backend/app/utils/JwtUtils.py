

from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv
import jwt


from os import environ

load_dotenv()

SECRET_KEY: str = environ.get("APP_CONFIG_SECRET_KEY")
ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_DAYS = 7

def create_access_token(data: dict):
    expire = datetime.now(timezone.utc) + timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    return jwt.encode(
        {"id": data.get('id'), "username": data.get('username'), "email":data.get('email'), "exp": expire, "type":"access"},
        SECRET_KEY
    )

def create_refresh_token(data: dict):
        expire = datetime.now(timezone.utc) + timedelta(days= REFRESH_TOKEN_EXPIRE_DAYS)
        return jwt.encode(
            {"id": data.get('id'), "username": data.get('username'), "email": data.get('email'), "exp": expire, "type":"refresh"},
            SECRET_KEY
        )

def decode_token(token):
        payload = jwt.decode(
            token,
            SECRET_KEY,
        )
        return payload


