from fastapi import FastAPI, HTTPException, Depends, Request

#from fastapi.responses import JSONResponse
#from fastapi_jwt_auth import AuthJWT
#from fastapi_jwt_auth.exceptions import AuthJWTException

from pydantic import BaseModel, EmailStr, Field
from typing import Annotated
from annotated_types import MaxLen, MinLen
from os import environ, path
from dotenv import load_dotenv

load_dotenv("/.env")

class UserNameSchema(BaseModel):
    username: str = Field(max_length = 20)
class UserEmailSchema(BaseModel):
    email: EmailStr = Field(max_length = 100, min_length = 8)
class UserPasswordSchema(BaseModel):
    password: str = Field(max_length = 100, min_length = 4)

class UserSchema(UserNameSchema, UserEmailSchema, UserPasswordSchema):
    ...

class UserDeleteSchema(UserEmailSchema, UserPasswordSchema):
    ...


class UserUpdateSchema(UserEmailSchema, UserPasswordSchema):
    new_username: str = Field(max_length = 20)
    new_password: str = Field(max_length = 100, min_length = 4)