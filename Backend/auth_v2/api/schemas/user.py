from pydantic import BaseModel, EmailStr
from typing import Optional


class LoginSchema(BaseModel):
    login :str

class PasswordSchema(BaseModel):
    password: str


class EmailSchema(BaseModel):
    email: EmailStr

class CreateUserSchema(LoginSchema, EmailSchema, PasswordSchema):
    ...


class UserLoginSchema(EmailSchema, PasswordSchema):
    ...

class UserOutSchema(BaseModel):
    # status: OK
    status: str    

# IN <-


class CRUD_AddUserSchema(CreateUserSchema):
    ...

class CRUD_DeleteUserSchema(UserLoginSchema):
    ...



class CRUD_UpdateUserSchema(CreateUserSchema):
    new_email: Optional[EmailSchema]
    new_login: Optional[LoginSchema]
    new_password: Optional[PasswordSchema]

# OUT ->

class CRUD_DeleteOutUserSchema(UserOutSchema):
    ...

class CRUD_UpdateOutUserSchema(UserOutSchema):
    ...
    
class CRUD_GetUserOutSchema(UserLoginSchema):
    ...

class UserLoginOutSchema(BaseModel):
    access_token: str
    refresh_token: str

    class Config:
        from_attributes = True


    
    












