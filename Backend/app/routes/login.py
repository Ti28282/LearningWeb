from fastapi import APIRouter, Depends, Response, Request, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from datetime import datetime, timezone, timedelta

from database.models.User import UserModel, RefreshToken
from settings.settings import AsyncSessionLocal, get_db
from schemas import LoginSchema
from utils.HashUtils import create_hash, verify
#from fastapi.security import OAuth2PasswordBearer

router = APIRouter(prefix = "/api/v0/user", tags = ["login"])
#oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "/login") 
# ADD REFRESH Login Logout Refresh_Token token: str = Depends(oauth2_scheme)

@router.get("/me")
async def get_current_user(
    db: AsyncSession = Depends(get_db)
    ):
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Cloud not validate credentials",
        headers = {
            "WWW-Authenticate":"Bearer"
        },
    )
    return []

@router.post("/login")
async def login(user_data: LoginSchema, response: Response, db: AsyncSession = Depends(get_db)):
    error = {"error": f"User {user_data.email} not found"}
    # Result Select(args - > Models db.execute(select(UserModel)))
    result = await db.execute(select(UserModel).where(
        UserModel.email == user_data.email
    ))

    user = result.scalar_one_or_none()

    if user == None:return error

    #! problem
    if verify(user_data.password, user.password):
        expire_at = datetime.now(timezone.utc) + timedelta(days = 7)
        Token = user.generate_token()
        refresh_token = user.create_refresh_token()
        
        hash_token = create_hash(refresh_token)

        db_token = RefreshToken(
            token = hash_token, 
            expires_at = expire_at,
            user_id = user.id
        )
        db.add(db_token)
        await db.commit(db_token)
        

        response.set_cookie(
            key = "refresh_token",
            value = Token.get("refresh_token"),
            httponly = True,
            secure = True,
            samesite = "strict",
            max_age = 60 * 60 * 24 * 7 # 7 days
            )

        
        return Token
    
    return {"error": "Wrong password"}


# ! Doing
@router.post("/logout")
async def logout(
    request: Request,
    response: Response,
    db: AsyncSession = Depends(get_db)):

    refresh_token = request.cookies.get("refresh_token")
    
    if refresh_token:
        result = await db.execute(select(RefreshToken))

        tokens = result.scalars().all()

        for rt in tokens:
            if verify(refresh_token, rt.token):
                await db.delete(rt)
                break
        await db.commit()

    response.delete_cookie("refresh_token")
    

    return {"message":"Logged out successfully"}


# ! Doing
@router.post("/refresh")
async def refresh_access_token(
    request: Request,
    response: Response, 
    db: AsyncSession = Depends(get_db)):
    token = request.cookies.get("refresh_token")

    if not token:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "Refresh token missing")
    
    result = await db.execute(select(RefreshToken))
    tokens = result.scalar().all()

    valid_token = None

    for rt in tokens:
        if verify(token, rt.token_hash):
            valid_token = rt
            break




@router.get("/")
async def read_user_me(current_user: UserModel = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email,
        "created_at": current_user.created_at
    }



















