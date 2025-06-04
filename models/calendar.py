from sqlalchemy import Column, Integer, String, Date
from pydantic import BaseModel
from typing import List
from datetime import date as date_type

from database.connection import Base

# Modelo SQLAlchemy para la base de datos
class DayRecord(Base):
    __tablename__ = "days"
    
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, unique=True, index=True)
    status = Column(String)

# Modelos Pydantic para API
class Day(BaseModel):
    id: int
    date: date_type
    status: str
    
    class Config:
        orm_mode = True

class CalendarResponse(BaseModel):
    days: List[Day]

class UpdateDayRequest(BaseModel):
    date: date_type
    status: str