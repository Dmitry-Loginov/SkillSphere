from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base

class Lesson(Base):
    __tablename__ = "lessons"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    learning_goals = Column(Text)
    theory_content = Column(Text)
    additional_resources = Column(Text)
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)
    order_index = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Связи
    subject = relationship("Subject", back_populates="lessons")
    tasks = relationship("Task", back_populates="lesson")