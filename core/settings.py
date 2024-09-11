import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    AWS_ACCESS_KEY: str = os.getenv("AWS_ACCESS_KEY")
    AWS_SECRET_KEY: str = os.getenv("AWS_SECRET_KEY")
    AWS_S3_IMAGE_BUCKET: str = os.getenv("AWS_S3_IMAGE_BUCKET")
    AWS_S3_METADATA_BUCKET: str = os.getenv("AWS_S3_METADATA_BUCKET")
    BLACK_AND_WHITE_DIR: str = os.getenv("BLACK_AND_WHITE_DIR")
    CARTOONIZATION_DIR: str = os.getenv("CARTOONIZATION_DIR")
    NUKKI_DIR: str = os.getenv("NUKKI_DIR")
    ORIGINAL_DIR: str = os.getenv("ORIGINAL_DIR")

settings = Settings()
