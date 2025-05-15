import uvicorn
from pydantic import BaseModel, EmailStr
from fastapi import FastAPI

app = FastAPI()


class CreateUser(BaseModel):
    email: EmailStr


@app.get('/')
def hello_index():
    """

    :return: на фронт отдаем json (конвертируется из dict)
    """
    return {
        'massege': 'Hallo, index',
    }


@app.get('/hello/')
def hello(name: str = 'World'):
    return {'message': f'Hello {name.strip().title()}!'}


@app.post('/users/')
def create_user(user: CreateUser):
    """
    Создание пользователя с валидацией email
    :param user:
    :return:
    """
    return {
        'message': 'success',
        'email': user.email,
    }


@app.post('/calc/add/')
def add(a: int, b: int):
    return {
        'a': a,
        'b': b,
        'a+b': a + b
    }


@app.get('/items/')
def list_items():
    return [
        'Item1',
        'Item2',
        'Item3',
    ]


@app.get('items/latest/')
def get_latest_item():
    return {
        'item': {
            'id': '0',
            'name': 'latest',
        }
    }


@app.get('/items/{item_id}/')
def get_item_by_id(item_id: int):
    return {
        'item': {
            'id': item_id,
        }
    }


# автоматический перезапуск
if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
