""" Модель создания сессии подключения к БД """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import settings

# Создаём движок SQLAlchemy для SQLite
engine = create_engine(settings.DATABASE_URL, echo=True)

# Создаём сессию
SessionLocal = sessionmaker(bind=engine)


# Функция для получения сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
