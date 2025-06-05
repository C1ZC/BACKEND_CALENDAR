# Calendario Semanal - Backend API

Este proyecto es una API REST desarrollada con FastAPI que gestiona un calendario semanal. Permite ver los días de la semana actual y actualizar su estado (disponible, ocupado, etc.).

## Características

- Obtener todos los días de la semana actual
- Actualizar el estado de un día específico
- Creación automática de registros para los días de la semana
- Base de datos SQLite para almacenamiento persistente

## Requisitos

El proyecto utiliza las siguientes tecnologías:
- Python 3.x
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn

## Video Instalaciòn

Puedes ver la instalacion en video del proyecto aquí:  
[https://youtu.be/qNWZaNM7Z58](https://youtu.be/qNWZaNM7Z58)


## Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/C1ZC/BACKEND_CALENDAR.git
cd BACKEND_CALENDAR
```

2. Crea un entorno virtual (opcional pero recomendado):
```bash
python -m venv .venv
# En Windows
.venv\Scripts\activate
# En macOS/Linux
source .venv/bin/activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Estructura del proyecto

```
backend_calendar/
├── main.py                  # Punto de entrada de la aplicación
├── calendar.db              # Base de datos SQLite
├── requirements.txt         # Dependencias del proyecto
├── database/
│   ├── __init__.py
│   └── connection.py        # Configuración de conexión a la BD
├── models/
│   ├── __init__.py
│   └── calendar.py          # Modelos de datos
└── routes/
    └── calendar.py          # Endpoints de la API
```

## Uso

1. Inicia el servidor:
```bash
python main.py
```

2. El servidor se ejecutará en `http://0.0.0.0:8000`

3. Accede a la documentación automática de la API:
```
http://localhost:8000/docs
```

## Endpoints de la API

### GET /api/calendar
Obtiene todos los días de la semana actual con su estado.

Respuesta:
```json
{
  "days": [
    {
      "id": 1,
      "date": "2023-06-12",
      "status": "Disponible"
    },
    ...
  ]
}
```

### POST /api/calendar
Actualiza el estado de un día específico.

Cuerpo de la solicitud:
```json
{
  "date": "2023-06-12",
  "status": "Ocupado"
}
```

Respuesta:
```json
{
  "id": 1,
  "date": "2023-06-12",
  "status": "Ocupado"
}
```

## Tecnologías utilizadas

- [FastAPI](https://fastapi.tiangolo.com/): Framework moderno y de alto rendimiento para crear APIs
- [SQLAlchemy](https://www.sqlalchemy.org/): ORM para interactuar con la base de datos
- [Pydantic](https://pydantic-docs.helpmanual.io/): Validación de datos
- [SQLite](https://www.sqlite.org/): Base de datos ligera
