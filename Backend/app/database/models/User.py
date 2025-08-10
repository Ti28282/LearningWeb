from sqlalchemy import ForeignKey, text, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import date
from app.database.database import int_pk, str_null_true, str_uniq, Base

class User(Base):
    id: Mapped[int_pk]
    email: Mapped[str_uniq]
    username: Mapped[str_null_true]
    password: Mapped[str_null_true]

    def __str__(self):
        return (f"{self.__class__.__name__}(id = {self.id}),"
                f"user_name = {self.username},"
                f"email = {self.email}")

    def __repr__(self):
        return str(self)