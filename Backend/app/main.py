import asyncio
import uvicorn
from routes.auth import auth
from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import JSONResponse
#from fastapi_jwt_auth.exceptions import AuthJWTException


# todo LOGGING FastAPI

app = FastAPI()
'''
@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )


'''
app.include_router(auth)

if __name__ == "__main__":
    try:
        uvicorn.run(
        app = app,
        host = "127.0.0.1",
        port = 5010
    ) 
    except KeyboardInterrupt:
        pass
