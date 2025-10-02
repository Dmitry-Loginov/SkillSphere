from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base

class Answer(Base):
    __tablename__ = "answers"
    
    id = Column(Integer, primary_key=True, index=True)
    file_path = Column(String(500), nullable=True)
    text_answer = Column(Text, nullable=True)
    student_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)
    grade = Column(Integer, nullable=True)
    teacher_comment = Column(Text)
    student_comment = Column(Text)
    submitted_at = Column(DateTime(timezone=True), server_default=func.now())
    graded_at = Column(DateTime(timezone=True), nullable=True)
    
    # Связи
    student = relationship("User", back_populates="answers")
    task = relationship("Task", back_populates="answers")