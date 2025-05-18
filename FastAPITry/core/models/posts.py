from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Post(Base):
    title: Mapped[str] = mapped_column(String(100), unique=False)
    body: Mapped[str] = mapped_column(
        Text,
        default="",  # используется, когда создаем новый экземпляр прямо в alchemy
        server_default="",  # используется на стороне сервера
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
