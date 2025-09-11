from pydantic import BaseModel, EmailStr



class LoginSchema(BaseModel):
    login :str

class PasswordSchema(BaseModel):
    password: str


class EmailSchema(BaseModel):
    email: EmailStr

class UserCreateSchema(LoginSchema, EmailSchema, PasswordSchema):
    ...


class UserLoginSchema(EmailSchema, PasswordSchema):
    ...

    

class UserLoginOutSchema(BaseModel):
    access_token: str
    refresh_token: str

    class Config:
        from_attributes = True

class UserOutSchema(BaseModel):
    
    status: str
    # status: OK
    











