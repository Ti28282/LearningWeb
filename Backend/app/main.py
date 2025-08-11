import asyncio
import uvicorn
from routes.auth import auth
from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import JSONResponse
#from fastapi_jwt_auth.exceptions import AuthJWTException
from contextlib import asynccontextmanager
from settings.settings import setting, ping_db, engine

from database.models.User import Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    # todo logging -> init_db 
    
    try:
        await ping_db()
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
            print("Tables checked/created")

    except Exception as e:
        print("Error connection", e)
        raise e
    yield

    # todo logging end
    print("Close connection")
    await engine.dispose()


app = FastAPI(title = "Auth Service", lifespan = lifespan)

app.include_router(auth)


if __name__ == "__main__":
    try:
        
        uvicorn.run(
        "main:app",
        host = "127.0.0.1",
        port = 5010
    ) 
    except KeyboardInterrupt:
        pass
