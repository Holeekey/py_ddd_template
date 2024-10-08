import uvicorn
import os
from fastapi import FastAPI
from dotenv import load_dotenv
from routes import main_router

load_dotenv()

app = FastAPI()

app.include_router(router=main_router)

if __name__ == "__main__":

   port = os.getenv('APP_PORT')

   if port is None:
      port = 8000
   else:
      port = int(port)

   uvicorn.run("main:app", host="127.0.0.1", port=port, reload=True)