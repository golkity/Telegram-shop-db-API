from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from app.database.requests import set_user, get_sneaker_item
from app.keyboards import get_sneaker_brands_keyboard, main, get_sneakers_keyboard, katalog

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await set_user(message.from_user.id)
    await message.answer(
        '🌟Привет, я твой персональный бот для покупки крутых кроссовок! 🚀 '
        'Я знаю все о последних трендах в мире кроссовок и помогу тебе подобрать '
        'идеальную пару для своего стиля. Просто задавай мне вопросы или используй команды, '
        'чтобы начать поиск и совершить покупку. Доверься мне, '
        'и ты обзаведешься самыми стильными и комфортными кроссовками! 🌟', reply_markup=main)


@router.message(F.text == "Каталог 🗂")
async def catalog(message: Message):
    await message.answer('Вы нажали на Каталог 🗂', reply_markup=katalog)


@router.message(F.text == "Обувь 👟")
async def catalog(message: Message):
    await message.answer('test text', reply_markup=await get_sneaker_brands_keyboard())


@router.callback_query(F.data.startswith('brand_'))
async def sneaker_menu(callback_query: CallbackQuery):
    brand_id = int(callback_query.data[len('brand_'):])
    await callback_query.message.answer("text test", reply_markup=await get_sneakers_keyboard(brand_id))


@router.callback_query(F.data.startswith('sneakers_'))
async def sneaker_menu(callback: CallbackQuery):
    # sneaker_id = callback.data[len('sneakers_'):]
    sneaker_item = await get_sneaker_item(callback.data.split('_')[1])
    await callback.answer('Вы выбрали товар')
    TEXT= (f"\n"
           f"Название: {sneaker_item.name}\n\n"
           f"Описание: {sneaker_item.description}\n\n"
           f"Цена: {sneaker_item.price}\n")

    await callback.message.answer_photo(photo=f'{sneaker_item.img_url}',caption=TEXT)
    # await callback.message.answer(f"Название: {sneaker_item.name}\n"
    #                               f"Описание: {sneaker_item.description}\n"
    #                               f"Цена: {sneaker_item.price}")


@router.message(F.text == 'Назад')
async def _back(message: Message):
    await message.answer('Вы вернулись в главное меню!', reply_markup=main)


