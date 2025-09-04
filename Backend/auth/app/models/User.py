from sqlalchemy import (
    String, 
    DateTime, 
    Column, 
    func, 
    Integer,
    Boolean, 
    ForeignKey
)

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from datetime import datetime, timezone



class Base(DeclarativeBase):
    pass

class UserModel(Base):
    __tablename__ = "user_account"

    id: int = Column(Integer,primary_key = True, autoincrement = True)
    username: str = Column(String(20), index = True)
    email: str = Column(String(100), unique = True, index = True)
    password: str = Column(String)
    is_active: bool = Column(Boolean, default = True)
    
    created_at: datetime = Column(
        DateTime(timezone = True), 
        default =  lambda: datetime.now(timezone.utc))
    
    updated_at: datetime = Column(
        DateTime(timezone= True), 
        server_default= func.now(),
        onupdate= lambda: datetime.now(timezone.utc), 
        nullable=False)
    refresh_token = relationship("RefreshTokenTable", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self): 
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"



class RefreshTokenTable(Base):
    __tablename__ = "refresh_tokens"

    id: int = Column(Integer,primary_key = True)
    token: str = Column(String,unique = True, index = True, nullable = True)
    expires_at: datetime = Column(DateTime(timezone = True))
    user_id: int = Column(Integer, ForeignKey("user_account.id")) 
    user = relationship("UserModel", back_populates = "refresh_token")

