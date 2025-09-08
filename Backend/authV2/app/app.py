from fastapi import FastAPI
import uvicorn
from tortoise.contrib.fastapi import register_tortoise
from config import config

from routing.user import router as user_routing
from fastapi.middleware.cors import CORSMiddleware


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
    modules={"models": ["src.models"]},  # Укажи папку с моделями
    generate_schemas=True,  # Автоматически создавать таблицы при запуске
    add_exception_handlers=True,  # Обработка ошибок базы
)



app.include_router(user_routing)

    
if __name__ == "__main__":
    uvicorn.run(
        app, 
        host = "127.0.0.1",
        port = 5101
        
        )