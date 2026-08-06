from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Enterprise Multi-Agent AI Platform"
    app_env: str = "development"
    app_version: str = "0.1.0"

    host: str = "127.0.0.1"
    port: int = 8000

    azure_openai_endpoint: str = ""
    azure_openai_api_key: str = ""
    azure_openai_deployment: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()

print(settings.app_name)