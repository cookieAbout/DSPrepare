""""""
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Product
from .schemas import ProductCreate, ProductUpdate, ProductPartial


async def get_products(session: AsyncSession) -> list[Product]:
    """ Чтение всех товаров """
    statement = select(Product).group_by(Product.id)
    result: Result = await session.execute(statement)
    product = result.scalars().all()
    return list(product)


async def get_product(session: AsyncSession, product_id: int) -> Product | None:
    """ Чтение одного товара по id """
    return await session.get(Product, product_id)


async def create_product(session: AsyncSession, product_in: ProductCreate) -> Product:
    """ Создание продукта """
    product = Product(**product_in.model_dump())
    session.add(product)
    await session.commit()
    # await session.refresh(product)
    return product


async def update_product(
        session: AsyncSession,
        product: Product,
        product_update: ProductUpdate | ProductPartial,
        partial: bool = False
) -> Product:
    """
    :param session:
    :param product:
    :param product_update:
    :param partial: частичное обновление (exclude_unset - игнорируем не переданное)
    :return:
    """
    for name, value in product_update.model_dump(exclude_unset=partial).items():
        setattr(product, name, value)

    await session.commit()
    return product


async def delete_product(
        session: AsyncSession,
        product: Product,
) -> None:
    await session.delete(product)
    await session.commit()
