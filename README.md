# Platilla de Proyecto de Python con DDD, FastAPI y Uvicorn

Este es un proyecto de ejemplo que utiliza FastAPI y Uvicorn para crear una API rápida y eficiente.

## Requisitos

- Python 3.12.6+
- FastAPI
- Uvicorn

## Instalación

1. Crea un entorno virtual:

   ```bash
   python -m venv env
   .venv\Scripts\Activate.ps1 // Windows
   source env/bin/activate // Linux
   ```

2. Activa el entorno virtual:

   Windows

   ```bash
   .venv\Scripts\Activate.ps1 // Windows
   source env/bin/activate // Linux
   ```

   macOS / Linux

   ```bash
   .venv\Scripts\Activate.ps1
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
├── app/
│   ├── main.py
│   ├── routers/
│   └── models/
├── tests/
├── requirements.txt
└── README.md
```

## Autor

Daniel Bruno, 2024
