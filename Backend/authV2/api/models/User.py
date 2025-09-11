
from tortoise.models import Model
from tortoise import fields



class UserModel(Model):
    id = fields.IntField(primary_key = True)




