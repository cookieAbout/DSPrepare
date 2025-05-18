from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings


BASE_DIR = Path(__file__).resolve().parent.parent  # получаем абсолютный путь

DB_PATH = BASE_DIR / "db.sqlite3"


class DBSettings(BaseModel):
    url: str = f"sqlite+aiosqlite:///{DB_PATH}"
    echo: bool = False  # True только для отладки


class Settings(BaseSettings):
    """Позволяет использовать env, брать от туда переменные, и валидацию"""

    api_v1_prefix: str = "/api/v1"
    db: DBSettings = DBSettings()


settings = Settings()
