from schemas import User

db = []
# connect to DB
def create_user(user_in: User) -> dict:
    user = user_in.model_dump()
    db.append(user)
    return {
        "success":True,
    }

def read_user() -> list:
    
    return {
        "user":db
    }

def update_user(user_in: User) -> dict:
    ...

def delete_user(user_in: User) -> dict:
    
    db.remove(user_in.model_dump())
    return {
        "success":True
    }


