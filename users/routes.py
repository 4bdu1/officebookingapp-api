from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTAuthentication
from users import models
from users import database
from fastapi import APIRouter
from .dependencies import on_after_forgot_password,on_after_forgot_password,after_verification_request, on_after_register




SECRET = "SECRET"

jwt_authentication = JWTAuthentication(
    secret=SECRET, lifetime_seconds=3600, tokenUrl="/auth/jwt/login")

fastapi_users = FastAPIUsers(
    database.user_db,
    [jwt_authentication],
    models.User,
    models.UserCreate,
    models.UserUpdate,
    models.UserDB,

    

)

router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(jwt_authentication), prefix="/auth/jwt", tags=["auth"]
)
router.include_router(
    fastapi_users.get_register_router(on_after_register), prefix="/auth", tags=["auth"]
)
router.include_router(
    fastapi_users.get_reset_password_router(
        SECRET, after_forgot_password=on_after_forgot_password
    ),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_verify_router(
        SECRET, after_verification_request=after_verification_request
    ),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(fastapi_users.get_users_router(), prefix="/users", tags=["users"])