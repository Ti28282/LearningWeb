from fastapi import FastAPI, HTTPException, Depends, Request

from pydantic import BaseModel, EmailStr, Field

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


class LoginSchema(UserEmailSchema, UserPasswordSchema):
    ...


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


