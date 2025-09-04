from schemas import UserSchema, UserDeleteSchema, UserUpdateSchema, UserModelSchema
from models.User import UserModel

from core.database import get_db
from core.security import create_hash
from core.config import settings
from settings.log import logger

from Backend.auth.app.exceptions import ConflictError, NotFoundError
from Backend.auth.app.dependencies import get_all_users, find_user, get_user_by_email

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update
from typing import Annotated, List
import httpx

router = APIRouter(prefix = '/api/v0', tags = ['auth'])

@router.post('/register')
async def create_user(
    user_data: UserSchema,
    db: AsyncSession = Depends(get_db)
) -> dict:
    print(f"{settings.URL_NOTIFICATION}/register")
    hashed_password = create_hash(str(user_data.password))
    
    user_exists = await get_user_by_email(email = user_data.email, db = db)

    if user_exists:
        raise ConflictError(detail = 'User already exists')
    
    
    user = UserModel(
        username = user_data.username,
        email = user_data.email,
        password = hashed_password
    )

    
    db.add(user)
    await db.commit()
    await db.refresh(user)

    # Notification
    try:
        pd = {
            "username": user_data.username,
            "email": user_data.email
            }
        
        async with httpx.AsyncClient as session:
            logger.info(f"{settings.URL_NOTIFICATION}/register")
            
            response = await session.post(f"{settings.URL_NOTIFICATION}/register", json = pd)

            logger.info(f"status code httpx.AsyncClient <{response.status}>")
            return {
                "success":True,
                "email": user.email,
                "create_at": user.created_at
            }

    except:
        logger.error(f"Server-Cors {settings.URL_NOTIFICATION}/notification") 
        return {
            "success":False,
            "Error":"Bad Notification Service"
        }

   
        
 
@router.get('/read_users')
async def get_users(users: Annotated[UserModel, Depends(get_all_users)]) -> List[UserModelSchema]:

    return [{
        "id":u.id, 
        "username": u.username, 
        "email": u.email, 
        "created_at": u.created_at, 
        "update_at": u.updated_at
        } for u in users]


@router.put('/update_user')
async def update_user(
    user_data: UserUpdateSchema, db: AsyncSession = Depends(get_db)):
    
    
    user = await find_user(user_data, db)

    await db.execute(update(UserModel).where(
       UserModel.email == user_data.email
    )
    .values(password = create_hash(str(user_data.new_password)), username = user_data.new_username)
    .execution_options(synchronize_session = 'fetch')
    )

    await db.commit()

    return {"message":f"User {user.email} update"}


@router.delete('/delete_user')
async def delete_user(
    user_data: UserDeleteSchema,
    db: AsyncSession = Depends(get_db)
):
    user = await get_user_by_email(email = user_data.email, db = db)

    if user is None:
        return NotFoundError()

    await db.delete(user)
    await db.commit()
        
    return {
        "success": True,
        "message": f"User {user.email} was deleted"
    }

    


