from fastapi import APIRouter, Depends, HTTPException, Request
#from fastapi_jwt_auth import AuthJWT
from schemas import User

auth = APIRouter(prefix = "/api/v0")

@auth.get("/test")
def test():
    return {"hello":"World"}

@auth.post("/login")
def login(user: User):
    return {user.login: user.password}

'''

@auth.post("/login/")
def login(user: User, Authorize):
    # CHECK validation from pydantic
    if user.username != "test" or user.password != "test":
        raise HTTPException(status_code=401, detail="Bad username or password")

    access_token = Authorize.create_access_token(subject = user.username)
    return {"access_token": access_token}
# : AuthJWT = Depends()
@auth.get("/protected/")
def protected(Authorize):
    Authorize.jwt_required()

    current_user = Authorize.get_jwt_subject()

    return {"user": current_user}

'''

