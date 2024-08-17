from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # SQLALCHEMY_DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    HOST: str
    DBNAME: str
    USER: str
    PASSWORD: str
    PORT: str

    class Config:
        env_file = ".env"


settings = Settings()
