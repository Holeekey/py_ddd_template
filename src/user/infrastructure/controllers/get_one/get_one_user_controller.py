from fastapi import FastAPI

async def get_one_user_controller(app: FastAPI):
    @app.get("/user", tags=["User"])
    async def execute():
        return {"message": "User found"}