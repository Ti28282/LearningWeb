from fastapi import APIRouter, Depends, Response, Request, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database.models.User import UserModel, hash_password, verify_password, RefreshToken

from settings.settings import AsyncSessionLocal, get_db
from schemas import LoginSchema


router = APIRouter(prefix = "/api/v0/user", tags = ["login"])

# ADD REFRESH Login Logout Refresh_Token

@router.post("/login")
async def login(user_data: LoginSchema, response: Response, db: AsyncSession = Depends(get_db)):
    error = {"error": f"User {user_data.email} not found"}
    result = await db.execute(select(UserModel).where(
        UserModel.email == user_data.email
    ))

    user = result.scalar_one_or_none()

    if user == None:return error
    #! problem
    if verify_password(user_data.password, user.password):
        db_token = RefreshToken(
            token = refresh_token, 
            expires_at = expires_at,
            user_id = user.id
        )
        return user.generate_token()
    
    return {"error": "Wrong password"}

@router.post("/logout")
def logout(user_data: LoginSchema, db: AsyncSession = Depends(get_db)):
    return []

@router.post("/refresh")
async def refresh_access_token(request: Request, db: AsyncSession = Depends(get_db)):
    token = request.cookies.get("refresh_token")

    if not token:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "Refresh token missing")
    result = await db.execute(select(RefreshToken))
    tokens = result.scalar().all()

    valid_token = None

    for rt in tokens:
        if verify_password(token, rt.token_hash):
            valid_token = rt
            break
























