from abc import ABC, abstractmethod
from typing import Optional
from schemas.user import UserCreateSchema, UserOutSchema



class UserRepository(ABC):


    @abstractmethod
    def create_user(self, user_data: UserCreateSchema) -> UserOutSchema:
        pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> Optional[UserOutSchema]:
        pass




