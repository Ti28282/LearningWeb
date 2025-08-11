
from schemas import UserSchema
from database.models.User import UserModel, hash_password, verify_password
from settings.settings import AsyncSessionLocal


from fastapi import APIRouter, Depends # HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

auth = APIRouter(prefix = "/api/v0", tags = ["auth"])
# Connect Postgres
# Validation
# save after enter code send to your email

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session



@auth.post("/user")
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

    

@auth.put("/update")
def update_user(user: UserSchema):
    return []

@auth.get("/users")
async def get_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(UserModel))
    users = result.scalars().all()
    
    return [{"id":u.id, "username": u.username, "email": u.email, "created_at": u.created_at} for u in users]

@auth.delete("/delete")
def delete_user(user: UserSchema):
    return []



