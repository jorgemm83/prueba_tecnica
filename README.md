# Prueba técnica

## Objetivo del proyecto

Desarrollar una aplicación web que demuestre habilidades en containerización con Docker, consumo de APIs externas y análisis de datos.

## Arquitectura:

project/
│
├── main.py              # Archivo principal para iniciar la aplicación
├── app/
│   ├── api/
│   │   └── endpoints.py  # Aquí se define el endpoint
│   ├── services/
│   │   └── financial.py  # Lógica de negocio (servicios)
        └── consumir_api.py # Lógica para consumir la API externa
│   ├── utils/
│   │   └── responses.py  # Manejo de respuestas comunes
│   └── __init__.py       # Permite que la carpeta `app/` sea un módulo de Python


## Ventajas de esta estructura:

* Modularidad: Separas responsabilidades. Cada archivo y carpeta tiene una función clara.
* Escalabilidad: A medida que el proyecto crezca, puedes añadir más servicios, controladores, y modelos sin que el archivo principal se vuelva inmanejable.
* Mantenibilidad: Facilita hacer cambios o depurar errores al tener un código bien organizado.
* Testabilidad: Con la lógica de negocio separada, es más fácil escribir pruebas unitarias para tus servicios sin involucrar la API.

## Desplegar solución:

Ejecutar el siguiente comando para desplegar el proyecto y publicar endpoint, utilizado docker compose

```bash
docker-compose up -d
```

Ejecutar el siguiente comando para desplegar el proyecto y publicar endpoint, sin docker compose 
1. Primer paso: Construir la imagen Docker

```bash
docker build -t mi-fastapi-app .
```

2 Paso: Ejecutar el contenedor:
```bash
docker run -d -p 8000:8000 mi-fastapi-app
```