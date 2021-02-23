from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator

class Roles(models.Model):

    id = fields.IntField(pk=True)
    role_name = fields.CharField(max_length=20)
    description = fields.CharField(max_length=100)


    class PydanticMeta:
        exclude = ["id"]
        

Role_Pydantic = pydantic_model_creator(Roles, name="Role")
RoleIn_Pydantic = pydantic_model_creator(Roles, name="Role_into_DB", exclude_readonly= True)
    