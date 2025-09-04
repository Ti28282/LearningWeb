from pydantic import BaseModel, EmailStr, Field
from dotenv import load_dotenv
from datetime import datetime


load_dotenv("/.env")

class UserNameSchema(BaseModel):
    username: str = Field(max_length = 20)
class UserEmailSchema(BaseModel):
    email: EmailStr = Field(max_length = 100, min_length = 8)
class UserPasswordSchema(BaseModel):
    password: str = Field(max_length = 100, min_length = 4)

class UserSchema(UserNameSchema, UserEmailSchema, UserPasswordSchema):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "username": "Timur",
                    "email": "test@gmail.com",
                    "password":"testAPI",
                }
            ]
        }
    }

class UserDeleteSchema(UserEmailSchema, UserPasswordSchema):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "test@gmail.com",
                    "password":"testAPI",
                }
            ]
        }
    }

class UserUpdateSchema(UserEmailSchema, UserPasswordSchema):
    new_username: str = Field(max_length = 20)
    new_password: str = Field(max_length = 100, min_length = 4)
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "test@gmail.com",
                    "password":"testAPI",
                    "new_username":"NewNameTim",
                    "new_password":"testAPINEW"
                }
            ]
        }
    }


class LoginSchema(UserEmailSchema, UserPasswordSchema):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "test@gmail.com",
                    "password":"testAPI",
                }
            ]
        }
    }

class TokenSchema(BaseModel):
    access_token: str
    type_token: str


class UserModelSchema(UserEmailSchema, UserNameSchema):
    id: int
    created_at: datetime
    update_at: datetime
