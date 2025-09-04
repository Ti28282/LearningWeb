from typing import Annotated, Optional
from fastapi import Depends, Body
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import asyncio

from core.security import oauth2_scheme, decode_token, verify_password
from core.database import get_db
from schemas import LoginSchema
from models.User import UserModel, RefreshTokenTable
from Backend.auth.app.exceptions import InvalidError, NotFoundError
from settings.log import logger

'''
async def current_user(
    token: Annotated[str, Depends(oauth2_scheme)], 
    db: Annotated[AsyncSession, Depends(get_db)]
) -> UserModel:
    try:
        payload = decode_token(token)
        email = payload.get("sub")
        if email is None:
            raise InvalidError(detail = "Failed to authorize credentials")
        # helpers.py get db
        result = await db.execute(select(UserModel).where(
            UserModel.email == email
        ))

        user =  result.scalar_one_or_none()

        if user is None:
            raise InvalidError(detail = "User not found")

        if not user.is_active:
            raise InvalidError(detail="User account is inactive")

        return user

    except Exception as e:

        logger.error(f"Internal server error: {str(e)}")
        raise InvalidError(detail=f"Internal server error")
'''        

async def get_all_users(db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(select(UserModel))
    return result.scalars().all()


async def get_user_by_email(
    email: str, 
    db: Annotated[AsyncSession, Depends(get_db)]
) -> Optional[UserModel]:
    
    result = await db.execute(select(UserModel).where(
        UserModel.email == email
    ))
    await asyncio.sleep(0.8)
    return result.scalar_one_or_none()


async def verify_user(user: UserModel, password: str) -> None:
    
    if user is None:
        logger.error(f"User {user.email} not found")
        raise NotFoundError(detail = f"User {user.email} not found")

    
    if not verify_password(plain_password = password.encode(), hashed_password = user.password.encode()):    
        logger.error("Incorrect email or password")
        raise InvalidError(detail = "Incorrect email or password")
    

# todo Connect Depends to login 
async def get_user_by_token(
    db: Annotated[AsyncSession, Depends(get_db)],      
    token: str
) -> RefreshTokenTable:
    
    result = await db.execute(select(RefreshTokenTable).where(
        RefreshTokenTable.token == token
    ))
    user = result.scalar_one_or_none()
    
    if user is None:

        raise InvalidError(detail = "User not found")
    
    await asyncio.sleep(0.8)

    return user


async def find_user(
        user_data: Annotated[LoginSchema, Body(embed=True)],
        db: Annotated[AsyncSession, Depends(get_db)]    
    ):
    
    user = await get_user_by_email(user_data.email, db)
    
    await verify_user(user = user, password = user_data.password)
    
    return user


async def async_dependency():
    await asyncio.sleep(1)
    return {"message":"test"}




