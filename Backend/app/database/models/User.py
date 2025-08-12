from sqlalchemy import String, ForeignKey, DateTime, Column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime, timezone, timedelta
from passlib.context import CryptContext
import jwt
from app.settings.settings import setting

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

class Base(DeclarativeBase):
    pass

class UserModel(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key = True, autoincrement = True)
    username: Mapped[str] = mapped_column(String(20), index = True)
    email: Mapped[str] = mapped_column(String(100), unique = True, index = True)
    password: Mapped[str] = mapped_column(String(128))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone = True), 
        default =  lambda: datetime.now(timezone.utc),  
        onupdate = lambda: datetime.now(timezone.utc)
    )

    def __repr__(self): 
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"

    def genetate_token(self):
        expire = datetime.now(timezone.utc) + timedelta(days = 30)
        return {
            "access_token": jwt.encode(
                {"id": self.id, "username": self.username, "email": self.email, "exp": expire},
                setting.SECRET_KEY()
                
            )
        }