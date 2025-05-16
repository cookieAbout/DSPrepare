from typing import Annotated
from annotated_types import MinLen, MaxLen
from pydantic import EmailStr, BaseModel  #, Field


class CreateUser(BaseModel):
    """ ... - обязательный параметр """
    # username: str = Field(..., min_length=3, max_length=20)
    user_name: Annotated[str, MinLen(1), MaxLen(20)]
    email: EmailStr
