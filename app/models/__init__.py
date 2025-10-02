# Импортируем Base из database
from app.database import Base

# Импортируем все модели
from app.models.user import User
from app.models.group import Group, user_to_group
from app.models.subject import Subject
from app.models.lesson import Lesson
from app.models.task import Task
from app.models.answer import Answer

# Список всех моделей для Alembic
__all__ = [
    "Base",
    "User",
    "Group", 
    "Subject",
    "Lesson",
    "Task",
    "Answer",
    "user_to_group",
]