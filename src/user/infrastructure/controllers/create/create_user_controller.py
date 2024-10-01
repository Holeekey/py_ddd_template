from fastapi import FastAPI
from ..prefix import USER_API_TAG, USER_PREFIX

async def create_user_controller(app: FastAPI):
    @app.post(USER_PREFIX, tags=[USER_API_TAG])
    async def execute():
        return {"message": "User created"}