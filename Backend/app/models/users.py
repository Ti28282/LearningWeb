from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from pydantic import BaseModel
from os import environ, path
from dotenv import load_dotenv

load_dotenv("/.env")


class User(BaseModel):
    login: str
    password: str

class Settings(BaseModel):
    authjwt_secret_key: str = environ.get("APP_CONFIG_SECRET_KEY")


@AuthJWT.load_config
def get_config():
    return Settings()