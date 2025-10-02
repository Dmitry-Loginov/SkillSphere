from pydantic import BaseModel, EmailStr
from typing import Optional
from fastapi_users import schemas

class UserRead(schemas.BaseUser[int]):
    id: int
    email: EmailStr
    full_name: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

class UserCreate(schemas.BaseUserCreate):
    email: EmailStr
    password: str
    full_name: str

class UserUpdate(schemas.BaseUserUpdate):
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    full_name: Optional[str] = None