import asyncio
import uvicorn

from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import JSONResponse
from fastapi_jwt_auth.exceptions import AuthJWTException


# todo LOGGING FastAPI

app = FastAPI()

@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )


async def main():
    uvicorn.run(
        app = app,
        host = "0.0.0.0",
        port = 5010,
        reload = True
    ) 


if __name__ == "__main__":
    try:
        asyncio.run(app)
    except KeyboardInterrupt:
        pass
