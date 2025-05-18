from typing import TYPE_CHECKING
from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .users import User


class Post(Base):
    title: Mapped[str] = mapped_column(String(100), unique=False)
    body: Mapped[str] = mapped_column(
        Text,
        default="",  # используется, когда создаем новый экземпляр прямо в alchemy
        server_default="",  # используется на стороне сервера
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="posts")
