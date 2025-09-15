
import uvicorn
from fastapi import FastAPI
import aiohttp
import requests

from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager


from routes import crud, login
from core.database import ping_db, engine

#from settings.log import LOGGING_CONFIG, logger

from models.User import Base
import models
# Connect Notification Tg

from fastapi.middleware.cors import CORSMiddleware




@asynccontextmanager
async def lifespan(app: FastAPI):
       
    # todo -> init_db
    try:
        await ping_db()
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
            
            #logger.info("Tables checked/created")
    except Exception as e:
        
        #logger.error("Error connection %s", str(e))


        raise e
    yield

    # todo logging end


    #logger.error("Close connection")
    await engine.dispose()





app = FastAPI(title = "Auth Service", lifespan = lifespan)

origins = [
    "http://0.0.0.0:3000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





app.include_router(crud.router)
app.include_router(login.router)


if __name__ == "__main__":
    try:
        
        uvicorn.run(
        "main:app",
        host = "192.168.101.14",
        port = 5010,
        reload = True,
        log_level="debug" 
        #log_config = LOGGING_CONFIG
    ) 
    except KeyboardInterrupt:
        pass
