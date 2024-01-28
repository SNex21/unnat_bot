from aiogram import Dispatcher, Bot, types
from dotenv import load_dotenv
import os
from aiogram.filters.command import Command
from aiogram.enums import ParseMode
from read1 import create_db
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile
from aiogram import F


load_dotenv()

bot = Bot(token=os.getenv('BOT_API'))
dp = Dispatcher(bot=bot)

skb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='💥 Поехали!', callback_data='poex')]])
kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=i, callback_data='ism')] for i in create_db()])
ism_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='🧭 Схема парка', callback_data='schema')],[InlineKeyboardButton(text='🏃 ЗОЖ активности', callback_data='zozh')],[InlineKeyboardButton(text='🌱 ЭКО активности', callback_data='eko')],[InlineKeyboardButton(text='🖌️ Создаём проекты', callback_data='poject')] ,[InlineKeyboardButton(text='❓ Квиз', callback_data='queeze')] ,[InlineKeyboardButton(text='🔎 Ищем сокровища', callback_data='sokr')],[InlineKeyboardButton(text='💡 Интерактив', callback_data='inter')]])
ret_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='↩️ Назад', callback_data='ism')]])
del_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='↩️ Назад', callback_data='del')]])



@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer('<b>Привет! Добро пожаловать в чат-бот "Все в парк!</b>".\n\nЗдесь ты можешь найти всю необходимую информацию о парках Москвы!\n\n<b>Нажми, чтобы начать!</b>', parse_mode=ParseMode.HTML, reply_markup=skb)


@dp.callback_query(F.data == 'poex')
async def ismail_park(cb: types.CallbackQuery):
    await cb.message.edit_text('<b>Добро пожаловать в чат-бот "Все в парк!</b>".\n\nЗдесь ты можешь найти всю необходимую информацию о парках Москвы!\n\n<b>Выберете парк из предложенного списка</b>', parse_mode=ParseMode.HTML, reply_markup=kb)


@dp.callback_query(F.data == 'ism')
async def ismail_park1(cb: types.CallbackQuery):
    await cb.message.edit_text('<b>👋 Добро пожаловать в Измайловский парк!</b>', parse_mode=ParseMode.HTML, reply_markup=ism_kb)


@dp.callback_query(F.data == 'schema')
async def ismail_park2(cb: types.CallbackQuery):
    await cb.message.edit_text('<b>Схему можете посмотреть по ссылке:\n https://moskvapark.naidich.ru/izmailovo/shemabig.htm</b>', parse_mode=ParseMode.HTML, reply_markup=ret_kb)


@dp.callback_query(F.data == 'zozh')
async def ismail_park3(cb: types.CallbackQuery):
    await cb.message.edit_text('<b>Бегайте по парку каждый день и будете здоровы!</b>', parse_mode=ParseMode.HTML, reply_markup=ret_kb)


@dp.callback_query(F.data == 'eko')
async def ismail_park4(cb: types.CallbackQuery):
    photo = FSInputFile(r'C:\Users\Producer\Desktop\UnnatBot\ы.png')

    await cb.message.answer_photo(photo=photo, caption='Относитесь к природе вежливо!', reply_markup=del_kb)


@dp.callback_query(F.data == 'project')
async def ismail_park5(cb: types.CallbackQuery):
    await cb.message.edit_text('<b>Мега проект</b>', parse_mode=ParseMode.HTML, reply_markup=ret_kb)


@dp.callback_query(F.data == 'queeze')
async def ismail_park6(cb: types.CallbackQuery):
    await cb.message.edit_text('<b>Квизы</b>', parse_mode=ParseMode.HTML, reply_markup=ret_kb)


@dp.callback_query(F.data == 'sokr')
async def ismail_park7(cb: types.CallbackQuery):
    await cb.message.edit_text('<b>Найди все сокровища парка!</b>', parse_mode=ParseMode.HTML, reply_markup=ret_kb)


@dp.callback_query(F.data == 'inter')
async def ismail_park8(cb: types.CallbackQuery):
    await cb.message.edit_text('<b>Приходи на наши субботники!</b>', parse_mode=ParseMode.HTML, reply_markup=ret_kb)


@dp.callback_query(F.data == 'del')
async def ismail_park9(cb: types.CallbackQuery):
    await bot.delete_message(cb.message.chat.id, cb.message.message_id) 


if __name__=='__main__':
    dp.run_polling(bot)