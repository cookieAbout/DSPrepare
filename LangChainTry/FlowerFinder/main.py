""" Модуль запуска тг-бота FlowerFinderBot """
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import settings
from bot.handlers import register_handlers
from database.schemas import Base
from database.session import engine


# Настройка логирования
logging.basicConfig(
    level=settings.LOG_LEVEL,
    format=settings.LOG_FORMAT
)
logger = logging.getLogger(__name__)

# Создаем таблицы в базе данных
try:
    Base.metadata.create_all(bind=engine)
    logger.info("База данных успешно инициализирована")
except Exception as exept:
    logger.error(f"Ошибка при инициализации базы данных: {exept}")
    raise

# Инициализация бота и диспетчера
try:
    bot = Bot(token=settings.BOT_TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
    logger.info("Бот успешно инициализирован")
except Exception as exept:
    logger.error(f"Ошибка при инициализации бота: {exept}")
    raise

# Регистрация обработчиков
register_handlers(dp)
logger.info("Обработчики команд зарегистрированы")


# Запуск бота
async def main():
    try:
        logger.info("Бот запущен")
        await dp.start_polling()
    except Exception as exept:
        logger.error(f"Ошибка при работе бота: {exept}")
    finally:
        session = await bot.get_session()
        await session.close()
        logger.info("Бот остановлен")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("\nХорошего дня!")
    except Exception as exept:
        logger.error(f"Неожиданная ошибка: {exept}")
