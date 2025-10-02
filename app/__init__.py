# app/__init__.py
"""
EduPlatform - Система дистанционного обучения
"""

__version__ = "1.0.0"
__author__ = "Dmitry Loginov"

# Можно добавить удобные импорты для быстрого доступа
from app.main import app
from app.core.config import settings

# Или оставить пустым - это тоже нормально