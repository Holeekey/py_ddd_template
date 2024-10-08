from fastapi import APIRouter
from user.infrastructure.routes.routes import main_router

router = APIRouter()
router.include_router(main_router)