import uvicorn
from fastapi import FastAPI

from items_views import router as items_router
from users.views import router as users_router

app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)


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


@app.post('/calc/add/')
def add(a: int, b: int):
    return {
        'a': a,
        'b': b,
        'a+b': a + b
    }


# автоматический перезапуск
if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
