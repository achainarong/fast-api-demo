from fastapi import APIRouter

from app.api.routes.users import router as usersRoutes

api_version = "/api/v1"

router = APIRouter()
router.include_router(
    usersRoutes,
    prefix=api_version,
    tags=["users"],
)
