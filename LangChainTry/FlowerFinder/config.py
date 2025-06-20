from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()


class Settings(BaseSettings):
    # Токен Telegram-бота
    BOT_TOKEN: str
    OPENAI_API_KEY: str
    GIGACHAT_API_PERS: str

    # Путь к базе данных SQLite
    DATABASE_URL: str = "sqlite:///flowers.db"

    # Настройки для бота
    BOT_ADMINS: list[int] = []  # Список ID администраторов
    BOT_PREFIX: str = "/"  # Префикс для команд
    BOT_NAME: str = "FlowerFinderBot"  # Имя бота

    # Настройки для логирования
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'


# Создаем экземпляр настроек
settings = Settings()
