from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from settings.log import logger
from core.config import settings


engine: AsyncEngine = create_async_engine(settings.DATABASE_URL, echo = True)

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

