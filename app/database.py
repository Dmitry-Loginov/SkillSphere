import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from fastapi_users.db import SQLAlchemyUserDatabase

# Создаем Base здесь
Base = declarative_base()

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

async def get_user_db():
    from app.models.user import User  # Локальный импорт чтобы избежать цикла
    yield SQLAlchemyUserDatabase(SessionLocal(), User)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()