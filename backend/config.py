from pydantic import BaseSettings

class Settings(BaseSettings):
    redis_url: str
    db_url: str
    capital: float
    market_hours: dict
    brokerage_costs: float
    risk_management: dict
    trading_parameters: dict

    class Config:
        env_file = ".env"

settings = Settings()