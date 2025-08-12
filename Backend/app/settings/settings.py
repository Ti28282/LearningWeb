from os import getenv, path
from dotenv import load_dotenv
import os



from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from settings.dictConfig import logger



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
    SECRET_KEY: str = getenv("APP_CONFIG_SECRET_KEY")
    
    @property
    def DATABASE_URL(self) -> str:
        return  f"postgresql+asyncpg://{self.PG_USER}:{self.PG_PASSWORD}@{self.PG_HOST}:{self.PG_PORT}/{self.PG_DB_NAME}"
    
    @property
    def SECRET_KEY(self) -> str:
        return self.SECRET_KEY


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
        logger.info("Postgress Connected %s", result.scalar())

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session