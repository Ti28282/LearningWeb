

from repositories.user_repository import UserRepository
from auth_v2.api.schemas.user import UserCreateSchema
from auth_v2.api.exceptions import ValidError



class UserService:


    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register_user(self, user_data: UserCreateSchema):
        

        if user_data.password < 6:
            raise ValidError()



        return self.user_repository.create_user(user_data)


    

