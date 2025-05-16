from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """ Позволяет использовать env, брать от туда переменные, и валидацию """
    db_url: str = 'sqlite+aiosqlite:///./db.sqlite3'
    db_echo: bool = False  # True только для отладки


settings = Settings()
