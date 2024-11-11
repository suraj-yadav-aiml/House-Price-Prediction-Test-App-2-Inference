from pydantic import DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict


class ModelSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="config/.env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    MODEL_PATH: DirectoryPath
    MODEL_NAME: str


model_settings = ModelSettings()

