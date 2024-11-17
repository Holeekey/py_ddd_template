import uvicorn
from fastapi import FastAPI
import config
from routes import router

app = FastAPI()

app.include_router(router=router, prefix=config.API_PREFIX)

if __name__ == "__main__":

    reload = config.STAGE == "dev"

    uvicorn.run("main:app", host="0.0.0.0", port=config.APP_PORT, reload=reload)
