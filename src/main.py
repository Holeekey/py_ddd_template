import uvicorn
import os
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/")
async def index():
   return {"message": "Hello World"}

if __name__ == "__main__":

   port = os.getenv('APP_PORT')

   if port is None:
      port = 8000
   else:
      port = int(port)

   uvicorn.run("main:app", host="127.0.0.1", port=port, reload=True)