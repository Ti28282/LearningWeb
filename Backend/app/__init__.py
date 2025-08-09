import asyncio
import uvicorn
from fastapi import FastAPI

# todo LOGGING FastAPI

app = FastAPI()




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
