from os import getenv, path
from dotenv import load_dotenv
import os
import logging
from logging.handlers import RotatingFileHandler

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

sqlalchemy_logger = logging.getLogger("sqlalchemy.engine")
sqlalchemy_logger.setLevel(logging.WARNING)
sqlalchemy_logger.disabled = True

file_handler = RotatingFileHandler("sqlalchemy.log", maxBytes=10485760, backupCount=5)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# Add Handler to logger
sqlalchemy_logger.addHandler(file_handler)

# clean duplicate logs
sqlalchemy_logger.propagate = False
class ExcludeSQLAlchemyFilter(logging.Filter):
    def filter(self, record):
        return not record.name.startswith("sqlalchemy")

logger = logging.getLogger("uvicorn")
logger.addFilter(ExcludeSQLAlchemyFilter())

dotenv_path = "./.env"
if path.exists(dotenv_path):
    load_dotenv(dotenv_path)

class Settings:
    
    PROJECT_VERSION: str = "0.0.1"

    PG_USER: str = getenv("APP_CONFIG_DB_USER")
    PG_PASSWORD: str = getenv("APP_CONFIG_DB_PASSWORD")
    PG_HOST: str = getenv("APP_CONFIG_DB_HOST", "192.168.101.100")
    PG_PORT: int = getenv("APP_CONFIG_DB_PORT", 5432)
    PG_DB_NAME: str = getenv("APP_CONFIG_DB_NAME")
    
    @property
    def DATABASE_URL(self):
        return  f"postgresql+asyncpg://{self.PG_USER}:{self.PG_PASSWORD}@{self.PG_HOST}:{self.PG_PORT}/{self.PG_DB_NAME}"



setting: Settings = Settings()




engine: AsyncEngine = create_async_engine(setting.DATABASE_URL, echo = True)
AsyncSessionLocal = sessionmaker(
    bind = engine,
    class_ = AsyncSession,
    expire_on_commit = False,
    autoflush = False
)

async def ping_db():
    async with engine.begin() as conn:
        result = await conn.execute(text("SELECT 1"))
        print("Postgress Connected", result.scalar())

