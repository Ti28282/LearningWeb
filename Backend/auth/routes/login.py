from fastapi import (
    APIRouter, 
    Depends, 
    Response, 
    Request, 
    HTTPException, 
    status
)
from fastapi.security import  HTTPBasic, HTTPBasicCredentials

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from datetime import datetime, timezone, timedelta
from typing import Dict, Annotated
import secrets

from database.models.User import UserModel, RefreshToken
from settings.settings import  get_db
from schemas import LoginSchema, UserSchema, TokenSchema
  
from utils import (
    create_access_token, 
    create_refresh_token, 
    decode_token, 
    PyJWTError,
    create_hash,
    verify
)
from exceptions import InvalidError, NotFoundError


router = APIRouter(prefix = '/api/v0/user', tags = ['login'])
security = HTTPBasic()
 
# ADD REFRESH Login Logout Refresh_Token token: str = Depends(oauth2_scheme)

async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(UserModel).where(UserModel.email == email))
    user =  result.scalar_one_or_none()
    return user



@router.post('/register')
async def register(
    user_data: UserSchema,
    db: AsyncSession = Depends(get_db)
):
    
    return []
#Annotated[HTTPBasicCredentials, Depends()]

@router.post('/login')
async def login(
    response: Response, 
    creds: LoginSchema, 
    db: AsyncSession = Depends(get_db)) -> Dict[str, str]:
    
    
    result = await db.execute(select(UserModel).where(
        UserModel.email == creds.email
    ))

    user = result.scalar_one_or_none()

    if user == None:
        raise NotFoundError(detail = f"User {creds.email} not found")

    
    elif not secrets.compare_digest(creds.password, user.password):
        raise InvalidError
        
    expire_at = datetime.now(timezone.utc) + timedelta(days = 7)
    Token = user.generate_token()
    
        
    
    hash_token = create_hash(Token.get("refresh_token"))

    db_token = RefreshToken(
            token = hash_token, 
            expires_at = expire_at,
            user_id = user.id
        )
    db.add(db_token)
    await db.commit()
    # FIX BUGS AUTH2password

    response.set_cookie(
            key = 'refresh_token',
            value = Token.get("refresh_token"),
            httponly = True,
            secure = True,
            samesite = 'strict',
            max_age = 60 * 60 * 24 * 7 # 7 days
            )

        
    return {
        "access_token": Token.get("access_token"),
        "token_type": "bearer"
        }
    
    


# ! Doing
@router.post('/logout')
async def logout(
    request: Request,
    response: Response,
    db: AsyncSession = Depends(get_db)):

    refresh_token = request.cookies.get("refresh_token")
    
    if refresh_token:
        result = await db.execute(select(RefreshToken))

        tokens = result.scalars().all()

        for rt in tokens:
            if secrets.compare_digest(refresh_token, rt.token):
                await db.delete(rt)
                break
        await db.commit()

    response.delete_cookie("refresh_token")
    

    return {'message':'Logged out successfully'}


# ! Doing
@router.post('/refresh')
async def refresh_access_token(
    request: Request,
    response: Response, 
    db: AsyncSession = Depends(get_db)):
    
    token = request.cookies.get("refresh_token")

    if not token:
        raise InvalidError(detail = 'Refresh token missing')
    
    result = await db.execute(select(RefreshToken))
    tokens = result.scalar().all()

    valid_token = None

    for rt in tokens:
        if secrets.compare_digest(token, rt.token_hash):
            valid_token = rt
            break


@router.get('/protect')
async def read_user_me(creds: HTTPBasicCredentials = Depends(security), db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(UserModel).where(
        UserModel.email == creds.username # Email
    ))

    user = result.scalar_one_or_none()

    if not user:
        raise NotFoundError
    
    elif not secrets.compare_digest(creds.password, user.password):
        raise InvalidError
    
    return {
        "email": creds.username    
        }



















