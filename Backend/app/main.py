import asyncio
import uvicorn
from routes import crud
from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import JSONResponse

from contextlib import asynccontextmanager
from settings.settings import setting, ping_db, engine
from settings.dictConfig import LOGGING_CONFIG, logger
from database.models.User import Base

import logging



@asynccontextmanager
async def lifespan(app: FastAPI):
    # todo logging -> init_db 
    
    try:
        await ping_db()
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
            
            logger.info("Tables checked/created")
    except Exception as e:
        print()
        logger.error("Error connection %s", str(e))
        raise e
    yield

    # todo logging end
    logger.error("Close connection")
    await engine.dispose()


app = FastAPI(title = "Auth Service", lifespan = lifespan)

app.include_router(crud.router)


if __name__ == "__main__":
    try:
        
        uvicorn.run(
        "main:app",
        host = "127.0.0.1",
        port = 5010,
        reload = True,
        log_config = LOGGING_CONFIG
    ) 
    except KeyboardInterrupt:
        pass
