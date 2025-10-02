import os
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = "postgresql://skillsphereuser:eduplatformpasswd@localhost/skillsphere"
    
    # JWT
    SECRET_KEY: str = "B4VGOfnejMs5rKtcu4oZSgfacJqMVUAqWgei2U5nhms"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8 * 8  # 64 days
    
    # FastAPI Users
    USERS_OPEN_REGISTRATION: bool = True
    
    class Config:
        env_file = ".env"

settings = Settings()