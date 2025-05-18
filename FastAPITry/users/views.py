from fastapi import APIRouter

from users.schemas import CreateUser
from users import crud
router = APIRouter(prefix='/users', tags=['Users'])


@router.post('/')
def create_user(user: CreateUser):
    """
    Создание пользователя с валидацией email
    :param user:
    :return:
    """
    return crud.create_user(user)
