from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    BASE_URL : str = os.environ.get("BASE_URL",default="")
    BASE_URL_LOCAL : str = os.environ.get("BASE_URL_LOCAL",default="")
    URL_RETRIEVE_YOUTUBE_CHANNEL : str =  os.environ.get("URL_RETRIEVE_YOUTUBE_CHANNEL",default="")
    URL_RETRIEVE_VIDEO  : str = os.environ.get("URL_RETRIEVE_VIDEO",default="")
    LOCAL : str = os.environ.get("LOCAL",default="")


settings=Settings()