from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="TERRA_", extra="ignore")

    ssb_base_url: str = "https://data.ssb.no/api/v0"
    norges_bank_base_url: str = "https://data.norges-bank.no/api/data"
    http_timeout_s: float = 60.0


settings = Settings()
