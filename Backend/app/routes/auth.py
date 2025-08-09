from fastapi import APIRouter, Depends, HTTPException, Request
from app import app
from fastapi_jwt_auth import AuthJWT
from models.users import User

auth = APIRouter("/api/v0/")




@auth.post("/login")
def login(user: User, Authorize: AuthJWT = Depends()):
    # CHECK validation from pydantic
    if user.username != "test" or user.password != "test":
        raise HTTPException(status_code=401, detail="Bad username or password")

    access_token = Authorize.create_access_token(subject = user.username)
    return {"access_token": access_token}

@auth.get("/protected")
def protected(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    current_user = Authorize.get_jwt_subject()

    return {"user": current_user}


app.include_router(auth)