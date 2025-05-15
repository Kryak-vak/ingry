from fastapi import APIRouter

from app.api.routes import nutrients, ingredients, recipes, users
from app.core.config import settings

api_router = APIRouter()
api_router.include_router(nutrients.router)
