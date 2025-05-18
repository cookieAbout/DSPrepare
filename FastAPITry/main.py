import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI

from core.config import settings
from api_v1 import router as router_v1
from items_views import router as items_router
from users.views import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # async with db_helper.engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all)  # создания и обновления работают через alembic

    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)
app.include_router(items_router)
app.include_router(users_router)


@app.get("/")
def hello_index():
    """

    :return: на фронт отдаем json (конвертируется из dict)
    """
    return {
        "massege": "Hallo, index",
    }


@app.get("/hello/")
def hello(name: str = "World"):
    return {"message": f"Hello {name.strip().title()}!"}


# автоматический перезапуск
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
