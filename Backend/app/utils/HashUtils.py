from passlib.context import CryptContext



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_hash(string: str) -> str:
    return pwd_context.hash(string)

def verify(plain_string: str, hashed_string: str) -> bool:
    return pwd_context.verify(plain_string, hashed_string)





