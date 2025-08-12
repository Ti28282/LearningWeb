
from schemas import UserSchema, UserDeleteSchema
from database.models.User import UserModel, hash_password, verify_password
from settings.settings import AsyncSessionLocal, get_db


from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

router = APIRouter(prefix = "/api/v0", tags = ["auth"])





@router.post("/register_user")
async def create_user(user_data: UserSchema, db: AsyncSession = Depends(get_db)):
    hashed_password = hash_password(user_data.password)
    user = UserModel(
        username = user_data.username,
        email = user_data.email,
        password = hashed_password
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)

    return {
        "success":True,
        "email": user.email,
        "create_at": user.created_at
    }

    
@router.get("/read_users")
async def get_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(UserModel))
    users = result.scalars().all()
    
    return [{"id":u.id, "username": u.username, "email": u.email, "created_at": u.created_at} for u in users]


@router.put("/update_user")
def update_user(user_data: UserSchema, db: AsyncSession = Depends(get_db)):
    return []


@router.delete("/delete_user")
async def delete_user(user_data: UserDeleteSchema ,db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(UserModel).where(
        UserModel.email == user_data.email,
        UserModel.username == user_data.username
    ))
    user = result.scalar_one_or_none()
    
    if not user: return {"error": f"User {user_data.username}---{user_data.email} not found"}
    
    await db.delete(user)
    await db.commit()
    
    return {
        "success": True,
        "message": f"User {user_data.email} was deleted"
    }



