from dotenv import load_dotenv

from os import environ, path
dotenv_path = "/.env"
if path.exists(dotenv_path):
    load_dotenv(dotenv_path)

APP_POSTGRES_URL_DB = f"postgresql+asyncpg://{environ.get("APP_CONFIG_DB_USER")}:{environ.get("APP_CONFIG_DB_PASSWORD")}@{environ.get("APP_CONFIG_DB_HOST")}:{environ.get("APP_CONFIG_DB_PORT")}/{environ.get("APP_CONFIG_DB_NAME")}"










