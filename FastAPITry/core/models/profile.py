from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .mixins import UserRelationMixin
from .base import Base


class Profile(UserRelationMixin, Base):
    _user_id_uniq = True
    _user_back_populates = "profile"

    first_name: Mapped[str | None] = mapped_column(String(40))
    last_name: Mapped[str | None] = mapped_column(String(40))
    bio: Mapped[str | None]
