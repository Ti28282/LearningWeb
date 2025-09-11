import os
from dotenv import load_dotenv


load_dotenv("./app/.envs/.env.dev")




class Test:
    DATABASE_URL = os.getenv("DATABASE_URL")


class Development:
    DATABASE_URL = os.getenv("DATABASE_URL")


class Production:
    pass



# Decide Config
class Config(Development):

    pass


config = Config()
    









