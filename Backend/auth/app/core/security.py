from passlib.context import CryptContext
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv
import jwt

from fastapi.security import  OAuth2PasswordBearer 

from os import environ


load_dotenv()

SECRET_KEY: str = environ.get("APP_CONFIG_SECRET_KEY")
ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_DAYS = 7

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def create_hash(string: str) -> str:
    return pwd_context.hash(string)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(email: str):
    expire = datetime.now(timezone.utc) + timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {}
    

    to_encode["sub"] = email
    to_encode["type"] = "access"
    to_encode["exp"] = expire
    to_encode["iat"] = datetime.now(timezone.utc)
    return jwt.encode(
        to_encode,
        SECRET_KEY
    )

def create_refresh_token(email: str):
        expire = datetime.now(timezone.utc) + timedelta(days= REFRESH_TOKEN_EXPIRE_DAYS)
        to_encode = {}

        to_encode["sub"] = email
        to_encode["type"] = "refresh"
        to_encode["exp"] = expire
        to_encode["iat"] = datetime.now(timezone.utc)

        return jwt.encode(
           to_encode,
            SECRET_KEY
        )

def decode_token(token: str):
        payload = jwt.decode(
            token,
            SECRET_KEY,
        )
        return payload

