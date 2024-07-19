from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.database.requests import get_sneaker_brands, get_sneakers

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог 🗂'),
                                      KeyboardButton(text='Доставка 🚚')],
                                     [KeyboardButton(text='Корзина 🗑'),
                                      KeyboardButton(text='Отзывы 📝')],
                                     [KeyboardButton(text='О нас 📲'),
                                      KeyboardButton(text='Часто задоваемые вопросы ❓')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню...')

katalog = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Футболки 👕"),
                                         KeyboardButton(text="Шорты 🩳")],
                                        [KeyboardButton(text="Обувь 👟"),
                                         KeyboardButton(text="Носки 🧦")],
                                        [KeyboardButton(text="Куртки 🥼"),
                                         KeyboardButton(text="Акссесуары 🎒")],
                                        [KeyboardButton(text="Назад")]],
                              resize_keyboard=True,
                              input_field_placeholder='Выберите пункт меню...')


async def get_sneaker_brands_keyboard():
    all_brands = await get_sneaker_brands()
    keyboard = InlineKeyboardBuilder()
    for brand in all_brands:
        keyboard.add(InlineKeyboardButton(text=brand.name, callback_data=f"brand_{brand.id}"))
    return keyboard.adjust(2).as_markup()


async def get_sneakers_keyboard(brand_id: int):
    all_sneakers = await get_sneakers(brand_id)
    keyboard = InlineKeyboardBuilder()
    for sneakers in all_sneakers:
        keyboard.add(InlineKeyboardButton(text=sneakers.name, callback_data=f"sneakers_{sneakers.id}"))
    return keyboard.adjust(2).as_markup()


