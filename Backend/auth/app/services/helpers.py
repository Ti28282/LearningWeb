from fastapi.security import  HTTPBasic
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

import secrets
from typing import Annotated


from schemas import LoginSchema
from core.database import  get_db
from models.User import UserModel, RefreshTokenTable
from Backend.auth.app.exceptions import NotFoundError, InvalidError

security = HTTPBasic()




async def delete_token(db: Annotated[AsyncSession, Depends(get_db)]):
    # todo Find the token and delete it when we log out or delete the endpoint
    # * /logout
    # * /delete_user
    
    pass



    

