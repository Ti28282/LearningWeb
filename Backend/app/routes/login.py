from fastapi import APIRouter, Depends, Response, Request, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database.models.User import UserModel, hash_password, verify_password, RefreshToken
from datetime import datetime, timezone, timedelta
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
        expire_at = datetime.now(timezone.utc) + timedelta(days = 7)
        refresh_token = user.create_refresh_token()
        hash_token = hash_password(refresh_token)

        db_token = RefreshToken(
            token = hash_token, 
            expires_at = expire_at,
            user_id = user.id
        )
        db.add(db_token)
        await db.commit(db_token)

        response.set_cookie(
            key = "refresh_token",
            value = refresh_token,
            httponly = True,
            secure = True,
            samesite = "strict",
            max_age = 60 * 60 * 24 * 7 # 7 days
            )


        return user.generate_token()
    
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
            if verify_password(refresh_token, rt.token):
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
        if verify_password(token, rt.token_hash):
            valid_token = rt
            break
























