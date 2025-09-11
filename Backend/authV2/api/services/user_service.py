

from repositories.user_repository import UserRepository
from schemas.user import UserCreateSchema




class UserService:


    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register_user(self, user_data: UserCreateSchema):
        

        if user_data.password < 6:
            raise 



        return self.user_repository.create_user(user_data)




