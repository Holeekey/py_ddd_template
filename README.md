# Platilla de Proyecto de Python con DDD, FastAPI y Uvicorn

Este es un proyecto de ejemplo que utiliza FastAPI y Uvicorn para crear una API rápida y eficiente.

## Requisitos

- Python 3.12.6+
- FastAPI
- Uvicorn

## Docker

1. Levantar contenedor

   ```bash
   docker compose up -d
   ```

2. Consultar contenedores levantados

   ```bash
   docker ps
   ```

3. Detener contenedor

   ```bash
   docker stop template-database
   ```

## Aplicar migraciones a base de datos

```bash
alembic upgrade head
```

## Correr aplicación

1. Crea un entorno virtual:

   ```bash
   python -m venv env
   ```

2. Activa el entorno virtual:

   Windows

   ```bash
   .venv\Scripts\Activate.ps1
   ```

   macOS / Linux

   ```bash
   source env/bin/activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución

Para iniciar el servidor, ejecuta el siguiente comando:

```bash
python src/main.py
```

Esto iniciará el servidor en `http://127.0.0.1:8000`.

## Formatear archivo

```bash
black [nombre_archivo].py
```

## Desactivar entorno virtual

Para desactivar el entorno virtual se ejecuta el siguiente comando:

```bash
deactivate
```

## Estructura del Proyecto

```
py_ddd_template/
├── src/
│   ├── main.py
│   ├── routes.py
│   └── user/
├── requirements.txt
└── README.md
```

## Autor

Daniel Bruno, 2024
