from fastapi import APIRouter

from FastAPITry.users.schemas import CreateUser
from FastAPITry.users import crud
router = APIRouter(prefix='/users', tags=['Users'])


@router.post('/')
def create_user(user: CreateUser):
    """
    Создание пользователя с валидацией email
    :param user:
    :return:
    """
    return crud.create_user(user)
