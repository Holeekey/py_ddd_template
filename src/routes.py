from fastapi import APIRouter
from user.infrastructure.routes.routes import user_router

router = APIRouter()
router.include_router(user_router)