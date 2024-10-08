from fastapi import APIRouter


main_router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)

@main_router.get("/one")
async def find_one_user():
    return {"id": 1, "name": "John Doe"}