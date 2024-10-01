import uvicorn
import os
from fastapi import FastAPI
from dotenv import load_dotenv
from contextlib import asynccontextmanager
from user.infrastructure.controllers.user_controllers import user_controllers
from user.infrastructure.controllers.prefix import USER_API_TAG

load_dotenv()

tags_metadata = [
    {
        "name": USER_API_TAG,
        "description": "Operations with users. The **login** logic is also here.",
    },
]

app = FastAPI(openapi_tags=tags_metadata)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Código que se ejecuta al iniciar la aplicación
    await user_controllers(app)
    yield
    # Código que se ejecuta al cerrar la aplicación (si es necesario)

app.router.lifespan_context = lifespan

if __name__ == "__main__":

   port = os.getenv('APP_PORT')

   if port is None:
      port = 8000
   else:
      port = int(port)

   uvicorn.run("main:app", host="127.0.0.1", port=port, reload=True)