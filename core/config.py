from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Omni LLM"
    APP_VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str
    GOOGLE_API_KEY: str
    MONGODB_URL: str
    MONGODB_NAME: str
    ALLOWED_ORIGINS: list = ["*"]
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "app.log"

    class Config:
        env_file = ".env"

settings = Settings()