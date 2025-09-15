
from tortoise.models import Model
from tortoise import fields



class UserModel(Model):

    __tablename__ = "user_account"


    id = fields.IntField(primary_key = True)
    login = fields.CharField(max_length = 20, nullable = False)
    email = fields.CharField(max_length=100, unique=True)
    password = fields.CharField(max_length = 300)
    is_active = fields.BooleanField(default=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.id

    class Meta:
        table = "tasks"

