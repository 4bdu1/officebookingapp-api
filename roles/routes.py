from fastapi import APIRouter,Depends
from roles.models import Roles, Role_Pydantic, RoleIn_Pydantic
from pydantic import BaseModel
from typing import List
from tortoise.contrib.fastapi import HTTPNotFoundError
from users import models,routes



router = APIRouter()


@router.post("/role", response_model = RoleIn_Pydantic, tags=['roles'])
async def create_role(role: RoleIn_Pydantic, user: models.User=Depends(routes.fastapi_users.get_current_superuser)):
    role_obj = await Roles.create(**role.dict())
    return role_obj

