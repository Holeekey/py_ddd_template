from fastapi import FastAPI
from user.infrastructure.controllers.create.create_user_controller import create_user_controller
from user.infrastructure.controllers.get_one.get_one_user_controller import get_one_user_controller

async def user_controllers(app: FastAPI):
    await get_one_user_controller(app)
    await create_user_controller(app)