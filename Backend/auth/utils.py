from passlib.context import CryptContext
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv
import jwt
from jwt.exceptions import PyJWTError


from os import environ


load_dotenv()

SECRET_KEY: str = environ.get("APP_CONFIG_SECRET_KEY")
ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_DAYS = 7

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_hash(string: str) -> str:
    return pwd_context.hash(string)

def create_access_token(data: dict):
    expire = datetime.now(timezone.utc) + timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {}
    to_encode.update(data)

    to_encode["sub"] = data.get("email")
    to_encode["type"] = "access"
    to_encode["exp"] = expire
    to_encode["iat"] = datetime.now(timezone.utc)
    return jwt.encode(
        to_encode,
        SECRET_KEY
    )

def create_refresh_token(data: dict):
        expire = datetime.now(timezone.utc) + timedelta(days= REFRESH_TOKEN_EXPIRE_DAYS)
        to_encode = data.copy()

        to_encode["sub"] = data.get("email")
        to_encode["type"] = "refresh"
        to_encode["exp"] = expire
        to_encode["iat"] = datetime.now(timezone.utc)

        return jwt.encode(
           to_encode,
            SECRET_KEY
        )

def decode_token(token):
        payload = jwt.decode(
            token,
            SECRET_KEY,
        )
        return payload

