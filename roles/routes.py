from typing import List

from fastapi import APIRouter, Body, Depends, Path
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from tortoise.contrib.fastapi import HTTPNotFoundError
from users import models, routes
from users.models import User, UserDB, UserModel, UserUpdate
from users.routes import fastapi_users

from roles.dependencies import a_new_role
from roles.models import Role_Pydantic, RoleIn_Pydantic, Roles

router = APIRouter(
    tags=['roles']
)

@router.get("/")
async def url_base():
    return {"message": "Welcome"}


@router.post("/role", response_model = RoleIn_Pydantic)
async def create_role(role: RoleIn_Pydantic, user: models.User=Depends(routes.fastapi_users.get_current_superuser)):
    role_obj = await Roles.create(**role.dict())
    return role_obj



@router.patch("/role/assign/") 
async def update_user_role(user_email :str, the_role =Depends(a_new_role)):   
    obj = await fastapi_users.get_user(user_email)
    update_object_to_dict = dict(obj)
    update_object_upacking = {**update_object_to_dict, "user_role":the_role}
    return update_object_upacking


    
