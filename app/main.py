from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.api.routes.api import router as api_router

# from app.core.config import app_settings


def init_app() -> FastAPI:
    application = FastAPI()
    application.include_router(api_router)

    return application


app = init_app()
