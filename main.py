from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.connection import engine
from models.calendar import Base
from routes.calendar import router as calendar_router

app = FastAPI()

# Permitir llamadas desde tu frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # cámbialo a tu dominio en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Incluir rutas
app.include_router(calendar_router, prefix="/api", tags=["calendar"])

@app.get("/")
def read_root():
    return {"message": "Hola desde FastAPI"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
