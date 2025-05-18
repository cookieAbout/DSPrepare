from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from .mixins import UserRelationMixin
from .base import Base


class Post(UserRelationMixin, Base):
    _user_back_populates = "posts"

    title: Mapped[str] = mapped_column(String(100), unique=False)
    body: Mapped[str] = mapped_column(
        Text,
        default="",  # используется, когда создаем новый экземпляр прямо в alchemy
        server_default="",  # используется на стороне сервера
    )
