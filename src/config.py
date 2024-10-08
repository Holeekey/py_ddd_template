from starlette.config import Config

config = Config(".env")

APP_PORT = config("APP_PORT", cast=int, default=8000)
STAGE = config("STAGE", default="dev")
API_PREFIX = config("API_PREFIX", default="/api/v1")