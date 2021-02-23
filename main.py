from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI
import users.models
import users.routes
import roles.models
import roles.routes


DB_NAME = "officebookingapp"



app = FastAPI(title = "Office Booking App")


DATABASE_URL = "sqlite://./test.db"

register_tortoise(   
    app,
    app.include_router(users.routes.router),
    app.include_router(roles.routes.router),
    db_url=DATABASE_URL,
    modules={"models": ["users.models","roles.models"]},
    generate_schemas=True,
    
)
