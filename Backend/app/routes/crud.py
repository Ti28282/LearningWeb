
from schemas import UserSchema, UserDeleteSchema, UserUpdateSchema
from database.models.User import UserModel
from settings.settings import  get_db
from utils.HashUtils import create_hash, verify


from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update

router = APIRouter(prefix = "/api/v0", tags = ["auth"])





@router.post("/register_user")
async def create_user(user_data: UserSchema, db: AsyncSession = Depends(get_db)):
    hashed_password = create_hash(user_data.password)
    user_search = await db.execute(select(UserModel).where(
        UserModel.email == user_data.email
    ))
    user = UserModel(
        username = user_data.username,
        email = user_data.email,
        password = hashed_password
    )

    if user_search:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = "User already exists"
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
    
    # Linux use tzdata
    return [{
        "id":u.id, 
        "username": u.username, 
        "email": u.email, 
        "created_at": u.created_at, 
        "update_at": u.updated_at
        } for u in users]


@router.put("/update_user")
async def update_user(user_data: UserUpdateSchema, db: AsyncSession = Depends(get_db)):
    error = {"error": f"User {user_data.email} not found"}
    
    user = await db.execute(select(UserModel).where(UserModel.email == user_data.email))
    user = user.scalar_one_or_none()

    
    
    
    if user is None: return error
    if not verify(user_data.password, user.password):
        return {"error": "Wrong password"}

    await db.execute(update(UserModel).where(
       UserModel.email == user_data.email
    )
    .values(password = create_hash(user_data.new_password), username = user_data.new_username)
    .execution_options(synchronize_session = "fetch")
    )

    await db.commit()

    return {"message":f"User {user_data.email} update"}


@router.delete("/delete_user")
async def delete_user(user_data: UserDeleteSchema, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(UserModel).where(
        UserModel.email == user_data.email
    ))

    user = result.scalar_one_or_none()
    
    if not user: return {"error": f"User {user_data.email} not found"}
    
    if verify(user_data.password, user.password):
        await db.delete(user)
        await db.commit()
        
        return {
            "success": True,
            "message": f"User {user_data.email} was deleted"
        }

    return {"error":"Wrong password"}


