from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
import datetime

Base = declarative_base()

class Todo(Base):
    __tablename__ = 'todos'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(String, nullable=False, default='pending')
    created_at = Column(String, default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))