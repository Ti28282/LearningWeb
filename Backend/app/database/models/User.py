from sqlalchemy import String, DateTime, Column, func, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from datetime import datetime, timezone, timedelta
from passlib.context import CryptContext
import jwt
from dotenv import load_dotenv
from os import environ

load_dotenv()

SECRET_KEY: str = environ.get("APP_CONFIG_SECRET_KEY")
ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_DAYS = 7

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

class Base(DeclarativeBase):
    pass

class UserModel(Base):
    __tablename__ = "user_account"

    id: int = Column(Integer,primary_key = True, autoincrement = True)
    username: str = Column(String(20), index = True)
    email: str = Column(String(100), unique = True, index = True)
    password: str = Column(String())
    created_at: datetime = Column(
        DateTime(timezone = True), 
        default =  lambda: datetime.now(timezone.utc))
    
    updated_at: datetime = Column(
        DateTime(timezone= True), 
        server_default= func.now(),
        onupdate= lambda: datetime.now(timezone.utc), 
        nullable=False)
    
    refresh_token = relationship("RefreshToken", back_populates = "user")

    def __repr__(self): 
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"

    def create_refresh_token(self):
        expire = datetime.now(timezone.utc) + timedelta(days= REFRESH_TOKEN_EXPIRE_DAYS)
        return jwt.encode(
            {"id": self.id, "username": self.username, "email": self.email, "exp": expire, "type":"refresh"},
            SECRET_KEY
        )

    def create_access_token(self):
        expire = datetime.now(timezone.utc) + timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
        return jwt.encode(
                {"id": self.id, "username": self.username, "email": self.email, "exp": expire, "type":"access"},
                SECRET_KEY
                )

    def generate_token(self):
        
        return {
            "access_token": self.create_access_token(),
            "token_type":"bearer"
            }
    

class RefreshToken(Base):
    __tablename__ = "refresh_tokens"

    id: int = Column(primary_key = True)
    token: str = Column(unique = True, index = True, nullable = True)
    expires_at: datetime = Column(
        DateTime(timezone = True)
    )
    user_id: int = Column(Integer, ForeignKey("user_account.id")) 
    user = relationship("User", back_populates = "refresh_tokens")

