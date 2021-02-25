from fastapi_users import models,FastAPIUsers
from fastapi_users.db import TortoiseBaseUserModel
from typing import Optional
from tortoise import fields

class User(models.BaseUser):
    user_role: Optional[str] = "regular user"
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    

class UserCreate(models.BaseUserCreate):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    
    

class UserUpdate(User, models.BaseUserUpdate):
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class UserDB(User, models.BaseUserDB):
    pass

class UserModel(TortoiseBaseUserModel):
    first_name= fields.CharField(null= False, max_length=30)
    last_name = fields.CharField(null= False, max_length=30)
    user_role= fields.CharField(null= False, max_length=30)
    