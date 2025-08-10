from fastapi import APIRouter, Depends, HTTPException, Request
#from fastapi_jwt_auth import AuthJWT
from schemas import User
from database.models import crud
auth = APIRouter(prefix = "/api/v0/users", tags = ["auth"])
# Connect Postgres
# Validation
# save after enter code send to your email


@auth.post("/add")
def create_user(user: User):
    return crud.create_user(user_in = user)

@auth.put("/update")
def update_user(user: User):
    return crud.update_user(user_in = user)

@auth.get("/get")
def search_user():
    return crud.read_user()

@auth.delete("/delete")
def delete_user(user: User):
    return crud.delete_user(user_in = user)


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

