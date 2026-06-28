from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # .env dosyasından okur; tanımlı olmayan ekstra değişkenleri yok sayar
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Veritabanı bağlantısı (dev: sqlite, prod: postgresql)
    DATABASE_URL: str = "sqlite:///./database.db"

    # JWT (kullanıcı auth)
    SECRET_KEY: str = "dev-insecure-change-me"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15

    # Service auth (authoritative game server -> maç girişi)
    GAME_SERVER_API_KEY: str = "dev-insecure-change-me"

    ADMIN_ROLE_LEVEL: int = 3

settings = Settings()
