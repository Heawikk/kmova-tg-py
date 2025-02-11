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
            fmt.text(f"👋 Привет, <b>{message.from_user.first_name}</b>", "\n\nВыберите интересующую вас информацию 👇"),
        ), parse_mode="HTML", reply_markup=builder.as_markup(resize_keyboard=True)
    )

# BOT START
async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())