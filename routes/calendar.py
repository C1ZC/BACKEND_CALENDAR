from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta, date

from database.connection import get_db
from models.calendar import DayRecord, Day, CalendarResponse, UpdateDayRequest

router = APIRouter()

# Función auxiliar para obtener las fechas de la semana actual
def get_current_week_dates():
    today = datetime.now().date()
    # Encontrar el lunes de la semana actual
    monday = today - timedelta(days=today.weekday())
    # Generar fechas para los 7 días de la semana
    week_dates = [monday + timedelta(days=i) for i in range(7)]
    return week_dates

@router.get("/calendar", response_model=CalendarResponse)
def get_calendar(db: Session = Depends(get_db)):
    # Obtener fechas de la semana actual
    week_dates = get_current_week_dates()
    
    # Verificar si existen registros para cada día de la semana
    # Si no existen, crearlos con estado "Disponible" por defecto
    for day_date in week_dates:
        day_record = db.query(DayRecord).filter(DayRecord.date == day_date).first()
        if not day_record:
            new_day = DayRecord(date=day_date, status="Disponible")
            db.add(new_day)
    db.commit()
    
    # Obtener todos los días de la semana actual
    days = db.query(DayRecord).filter(DayRecord.date.in_(week_dates)).all()
    
    return {"days": days}

@router.post("/calendar", response_model=Day)
def update_day_status(update_data: UpdateDayRequest, db: Session = Depends(get_db)):
    # Buscar el día en la base de datos
    day_record = db.query(DayRecord).filter(DayRecord.date == update_data.date).first()
    
    # Si no existe, crear un nuevo registro
    if not day_record:
        day_record = DayRecord(date=update_data.date, status=update_data.status)
        db.add(day_record)
    else:
        # Actualizar el estado del día existente
        day_record.status = update_data.status
    
    db.commit()
    db.refresh(day_record)
    
    return day_record