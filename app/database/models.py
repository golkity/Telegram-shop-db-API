from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
import os
from dotenv import load_dotenv
load_dotenv()

engine = create_async_engine(url=os.getenv('SQLALCHEMY_URL'))

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)


class SneakerBrand(Base):
    __tablename__ = 'sneaker_brands'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(25))
    sneakers = relationship("Sneaker", back_populates="brand")


class Sneaker(Base):
    __tablename__ = 'sneaker_items'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(25))
    description: Mapped[str] = mapped_column(String(25))
    price: Mapped[int] = mapped_column()
    img_url: Mapped[str] = mapped_column(String(99))
    brand_id: Mapped[int] = mapped_column(ForeignKey('sneaker_brands.id'))
    brand = relationship(SneakerBrand, back_populates="sneakers")


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
