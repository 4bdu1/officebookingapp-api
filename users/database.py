from fastapi_users.db import TortoiseBaseUserModel, TortoiseUserDatabase
from tortoise.contrib.fastapi import register_tortoise
from users.models import UserDB,UserModel
from tortoise import fields, models




user_db = TortoiseUserDatabase(UserDB, UserModel)