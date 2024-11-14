import uvicorn
from fastapi import FastAPI
from routes import user_router
import config

app = FastAPI()

app.include_router(router=user_router, prefix=config.API_PREFIX)

if __name__ == "__main__":

   reload = config.STAGE == "dev"

   uvicorn.run("main:app", host="127.0.0.1", port=config.APP_PORT, reload=reload)