from app.database.models import async_session
from app.database.models import User, SneakerBrand, Sneaker
from sqlalchemy import select


async def set_user(tg_id: int) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()


async def get_sneaker_brands():
    async with async_session() as session:
        return await session.scalars(select(SneakerBrand))


async def get_sneakers(brand_id: int):
    async with async_session() as session:
        return await session.scalars(select(Sneaker).where(Sneaker.brand_id == brand_id))


async def get_sneaker_item(sneaker_id: int):
    async with async_session() as session:
        return await session.scalar(select(Sneaker).where(Sneaker.id == sneaker_id))
