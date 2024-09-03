import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    AWS_ACCESS_KEY: str = os.getenv("AWS_ACCESS_KEY")
    AWS_SECRET_KEY: str = os.getenv("AWS_SECRET_KEY")
    AWS_S3_BUCKET: str = os.getenv("AWS_S3_BUCKET")
    BLACK_AND_WHITE_DIR: str = os.getenv("BLACK_AND_WHITE_DIR")
    CARTOONIZATION_DIR: str = os.getenv("CARTOONIZATION_DIR")
    NUKKI_DIR: str = os.getenv("NUKKI_DIR")

settings = Settings()
