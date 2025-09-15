from abc import ABC, abstractmethod
from typing import Optional, List
from auth_v2.api.schemas.user import (
    CreateUserSchema, 
    UserOutSchema, 
    UserLoginSchema,
    UpdateUserSchema,
   
    )


class CRUDRepository(ABC):

    @abstractmethod
    def add(self, user_data: CreateUserSchema) -> UserOutSchema:
        pass
    
    @abstractmethod
    def get(self) -> UserOutSchema:
        pass

    @abstractmethod
    def delete(self, user_data: UserLoginSchema) -> UserOutSchema:
        pass

    @abstractmethod
    def put(self, user_data: UpdateUserSchema) -> UserOutSchema:
        pass

class UserRepository(ABC):


    @abstractmethod
    def create_user(self, user_data: CreateUserSchema) -> UserOutSchema:
        pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> Optional[UserOutSchema]:
        pass
