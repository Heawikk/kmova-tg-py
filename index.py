# LIBRARIES
import asyncio
import logging
import sys
import random
import time
import threading
from aiogram import Bot, Dispatcher, html, types
from aiogram.client.default import DefaultBotProperties
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import FSInputFile
from aiogram import F
import aiogram.utils.markdown as fmt
from config import settings 

# API
TOKEN = settings['token']
dp = Dispatcher()

###################
###### START ######
###################

@dp.message(Command("start"))
async def start_command(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="📃 Информация"))
    builder.row(types.KeyboardButton(text="🎖️ Ветераны"))
    builder.row(types.KeyboardButton(text="📚 Книги ВОВ"))
    
    await message.reply(
        fmt.text(
            fmt.text(f"👋 Привет, <b>{message.from_user.first_name}</b>", "\n\nВыберите интересующую вас информацию 👇"),
        ), parse_mode="HTML", reply_markup=builder.as_markup(resize_keyboard=True)
    )

@dp.message(F.text == '↩️ Назад (Главное меню)')
async def start_command(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="📃 Информация"))
    builder.row(types.KeyboardButton(text="🎖️ Ветераны"))
    builder.row(types.KeyboardButton(text="📚 Книги ВОВ"))
    
    await message.reply(
        fmt.text(
            fmt.text(f"Выберите интересующую вас информацию 👇"),
        ), parse_mode="HTML", reply_markup=builder.as_markup(resize_keyboard=True)
    )

@dp.message(F.text == '📃 Информация')
async def start_command(message: types.Message):
    builder = ReplyKeyboardBuilder()
    
    builder.row(types.KeyboardButton(text="↩️ Назад (Главное меню)"))

    image_from_pc = FSInputFile("src/main/Picture.png")
    

    await message.answer_photo(image_from_pc,caption="<b>Участие жителей Анабарского улуса в Великой Отечественной Войне</b>\n\nНа территории Анабарского улуса никогда не было военных действий, как не было их и на огромных пространствах Якутии. Но война вошла в каждый улус, в каждую семью республики – голодом, карточной системой обеспечения продуктами, почти круглосуточным трудом.\nСоветский Союз не призывал на фронт представителей коренных малых народов Севера, уходили на войну отдельные добровольцы. Но все население поголовно работало для фронта с напряжением всех сил. \nВ общей сложности, Анабарский улус собрал и отправил фронту:\n- денежных средств – 264 980 рублей,\n- теплых вещей – 5858 шт.,\n- на строительство танка «Советская Якутия» - 196 007 рублей.", reply_markup=builder.as_markup(resize_keyboard=True))

@dp.message(F.text == '🎖️ Ветераны')
async def start_command(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="Андросова Федора Николаевна"))
    builder.row(types.KeyboardButton(text="Андросова Марфа Михайловна"))
    builder.row(types.KeyboardButton(text="Андросова Мария Михайловна"))
    builder.row(types.KeyboardButton(text="Андросова Евдокия Васильевна"))
    builder.row(types.KeyboardButton(text="Андросова Варвара Федоровна"))
    builder.row(types.KeyboardButton(text="Акакиева Софья Павловна"))
    builder.row(types.KeyboardButton(text="Акакиева Татьяна Егоровна"))
    builder.row(types.KeyboardButton(text="Анисимов Егор Иннокентьевич"))
    builder.row(types.KeyboardButton(text="Анисимова Татьяна Федоровна"))
    builder.row(types.KeyboardButton(text="Антонов Никифор Филиппович"))
    builder.row(types.KeyboardButton(text="Арьянова Екатерина Алексеевна"))
    builder.row(types.KeyboardButton(text="Арьянов Иван Васильевич"))
    builder.row(types.KeyboardButton(text="Борисова Мавра Ивановна"))
    builder.row(types.KeyboardButton(text="Винокурова Екатерина"))
    builder.row(types.KeyboardButton(text="Винокуров Николай Иннокентьевич"))
    builder.row(types.KeyboardButton(text="Винокуров Константин Николаевич"))
    builder.row(types.KeyboardButton(text="Винокуров Дмитрий Егорович"))
    builder.row(types.KeyboardButton(text="Винокуров Василий Николаевич"))
    builder.row(types.KeyboardButton(text="Винокуров Егор Романович"))
    builder.row(types.KeyboardButton(text="↩️ Назад (Главное меню)"))
    
    await message.reply(
        fmt.text(
            fmt.text(f"👋 Привет, <b>{message.from_user.first_name}</b>", "\n\nВыберите интересующую вас информацию 👇"),
        ), parse_mode="HTML", reply_markup=builder.as_markup(resize_keyboard=True)
    )

# BOT START
async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())