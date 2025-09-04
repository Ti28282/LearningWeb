from os import getenv, path
from dotenv import load_dotenv


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


    URL_NOTIFICATION: str = getenv("CORS_NOTIFICATION")

    @property
    def DATABASE_URL(self) -> str:
        return  f"postgresql+asyncpg://{self.PG_USER}:{self.PG_PASSWORD}@{self.PG_HOST}:{self.PG_PORT}/{self.PG_DB_NAME}"
    
    
    @property
    def SECRET_KEY(self) -> str:
        return self.SECRET_KEY
    
    


settings: Settings = Settings()



