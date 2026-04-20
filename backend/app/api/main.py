from fastapi import APIRouter
from app.api.routes.example_auth import hello_world

api_router = APIRouter()

api_router.include_router(hello_world.router)