from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

from tortoise.contrib.fastapi import register_tortoise

from config import config

from Backend.auth_v2.api.routing.users import router as user_routing


app = FastAPI(title = "AuthV2", openapi_url="/core/openapi.json", docs_url="/core/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




register_tortoise(
    app,
    db_url = config.DATABASE_URL,
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,  
)



app.include_router(user_routing)

    
if __name__ == "__main__":
    uvicorn.run(
        app, 
        host = "127.0.0.1",
        port = 5101
        
        )