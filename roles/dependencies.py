from roles.models import Roles,Role_Pydantic
from fastapi import status,HTTPException


async def a_new_role(role: str):
    role_object = await Role_Pydantic.from_queryset_single(Roles.get(role_name = role))
    new_role = dict(role_object)
    return new_role["role_name"]
    if not role:
        print({"Error":"THE ROLE DOES EXIST YET. KINDLY CREATE"})
        raise HTTPException(status_code=400, detail="The Role hasn't been created", headers={"X-Error": "There goes my error"})

    