from fastapi import FastAPI
from app.api import endpoints

app = FastAPI()

# Registrar las rutas
app.include_router(endpoints.router)
