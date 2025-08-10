from dotenv import load_dotenv

from os import getenv, path
dotenv_path = "/.env"
if path.exists(dotenv_path):
    load_dotenv(dotenv_path)
