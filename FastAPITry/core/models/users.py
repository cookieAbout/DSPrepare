from typing import TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from posts import Post
    from profile import Profile


class User(Base):
    user_name: Mapped[str] = mapped_column(String(32), unique=True)
    # Получаем список из постов
    posts: Mapped[list["Post"]] = relationship(back_populates="users")
    profile: Mapped["Profile"] = relationship(back_populates="users")
