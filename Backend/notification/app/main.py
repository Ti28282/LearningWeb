from fastapi import FastAPI
import httpx
import uvicorn
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os
from logging import Logger

from datetime import datetime
import time
load_dotenv()


logger = Logger(__name__)


app = FastAPI(title = "Notification Service")

TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
TELEGRAM_CHAT_URL = os.getenv("TELEGRAM_CHAT_URL")

#time_test = f"({result.day}.{result.month}.{result.year}) -- < {result.hour}:{result.minute} >"
class LoginRequest(BaseModel):
    username: str
    

class RegisterRequest(BaseModel):
    username: str
    email: str

class LogoutRequest(RegisterRequest):
    ...

payload = {
        "chat_id":TELEGRAM_CHAT_ID,
        "text":"",
        "parse_mode":"HTML"
    } 


async def send_message(pd: dict):
    
    async with httpx.AsyncClient() as session:

        response = await session.post(TELEGRAM_CHAT_URL, json = pd)
           
            
       # logger.info(f"status code <{response.status_code}>")
        logger.info("GOOD")


"""
/register post data.username && data.email httpx
"""

@app.post("/notification/register")
async def register(data: RegisterRequest):
    logger.info(f"{data.username}:{data.email}-->")
    message = (
        f"🆕 <b>Новая регистрация</b>\n"
        f"Пользователь: {data.username}\n"
        f"Email: {data.email}"
    )
    
    payload["text"] = message
    await send_message(payload)

    return {"message": "Пользователь зарегистрирован", "user": data.username}

@app.post("/notification/login")
async def login(data: LoginRequest):

    
    
    message = (
        f"🚪 <b>Вход в систему</b>\n"
        f"Пользователь: {data.username}\n"
        f"Время: {datetime.now().strftime(' %Y.%m.%d   %H:%M ')}"
    )

    payload["text"] = message
    await send_message(payload)

    return {"message": "Успешный вход", "user": data.username}

@app.post("/notification/logout")
async def logout(data: LogoutRequest):
    return 0


@app.get("/")
def status():
    return {"status":"service work"}



if __name__ == "__main__":
    uvicorn.run(app, port = 5002)







