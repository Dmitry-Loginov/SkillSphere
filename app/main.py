from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from app.auth.config import auth_backend
from app.auth.manager import get_user_manager
from app.models.user import User
from app.schemas.user import UserRead, UserCreate, UserUpdate

# Инициализация FastAPI Users
fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app = FastAPI(title="EduPlatform API", version="1.0.0")

# Подключаем роутеры аутентификации
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to EduPlatform API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}