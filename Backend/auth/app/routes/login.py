from fastapi import (
    APIRouter, 
    Depends, 
    Response, 
    Request, 
    HTTPException, 
    status
)
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from datetime import datetime, timezone, timedelta
from typing import Dict, Annotated
import secrets

from models.User import UserModel, RefreshTokenTable
from schemas import LoginSchema, TokenSchema
from Backend.auth.app.dependencies import find_user, get_user_by_token, find_user, async_dependency
from core.security import create_hash, create_access_token, create_refresh_token
from core.database import get_db
from Backend.auth.app.exceptions import InvalidError, NotFoundError


router = APIRouter(prefix = '/api/v0/user', tags = ['login'])


@router.post('/login')
async def login(
    user_data: Annotated[LoginSchema, Depends(find_user)],
    db: Annotated[AsyncSession, Depends(get_db)]
) -> TokenSchema:
    
    content = {
        "access_token": "",
        "token_type": "bearer"
    }
    
    


    
    expire_at = datetime.now(timezone.utc) + timedelta(days = 7)
    
    TokenAccess = create_access_token(user_data.email).decode()
    TokenRefresh = create_refresh_token(user_data.email).decode()

    
    content['access_token'] = TokenAccess

    response = JSONResponse(
            content = content,
            status_code = status.HTTP_200_OK
        )

    # Search Token from DB if exists
    result = await db.execute(select(RefreshTokenTable).where(
        RefreshTokenTable.token == TokenRefresh
    ))
    
    token = result.scalar_one_or_none()

    # Create token save to DB
    if token is None:
        hash_token = create_hash(TokenRefresh)
        
        db_token = RefreshTokenTable(
            token = hash_token, 
            expires_at = expire_at,
            user_id = user_data.id
        )
        db.add(db_token)
        await db.commit()
        

        response.set_cookie(
            key = 'refresh_token',
            value = TokenRefresh,
            httponly = True,
            secure = True,
            samesite = 'strict',
            max_age = 60 * 60 * 24 * 7 # 7 days
        )

        return response

    

    response.set_cookie(
            key = 'refresh_token',
            value = TokenRefresh,
            httponly = True,
            secure = True,
            samesite = 'strict',
            max_age = 60 * 60 * 24 * 7 # 7 days
            )

    
        
    return response



# ! Doing
@router.post('/logout')
async def logout(
    request: Request,
    response: Response,
    tokens: Annotated[RefreshTokenTable, Depends(get_user_by_token)],
    db: Annotated[AsyncSession, Depends(get_db)]
):

    refresh_token = request.cookies.get("refresh_token")
    
    if refresh_token:

        

        for RemoveToken in tokens:
            if secrets.compare_digest(refresh_token, RemoveToken.token):
                await db.delete(RemoveToken)
                break
        await db.commit()

    response.delete_cookie("refresh_token")
    

    return {'message':'Logged out successfully'}


# ! Doing
@router.post('/refresh')
async def refresh_access_token(
    request: Request,
    db: Annotated[AsyncSession, Depends(get_db)]
):
    
    token = request.cookies.get("refresh_token")

    if not token:
        raise InvalidError(detail = 'Refresh token missing')
    
    result = await db.execute(select(RefreshTokenTable))
    tokens = result.scalar_one_or_none()

    valid_token = None

    for rt in tokens:
        if secrets.compare_digest(token, rt.token_hash):
            valid_token = rt
            break


# @router.get('/protect')
# async def read_user_me(
#     creds: Annotated[HTTPBasicCredentials, Depends(security)], 
#     db: Annotated[AsyncSession, Depends(get_db)]
# ):
#     result = await db.execute(select(UserModel).where(
#         UserModel.email == creds.username # Email
#     ))

#     user = result.scalar_one_or_none()

#     if not user:
#         raise NotFoundError
    
#     elif not secrets.compare_digest(creds.password, user.password):
#         raise InvalidError
    
#     return {
#         "email": creds.username    
#         }

@router.post('/test')
async def testdata(
    dep: Annotated[str, Depends(async_dependency)]
):
    return dep


















