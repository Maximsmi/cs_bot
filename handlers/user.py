# Router используется для удобного масштабирования проекта.
# Благодаря ему, мы можем отказаться от необходимости импортировать Dispatcher в каждом хендлере.
# Вместо этого роутеры берут на себя эту роль, упрощая структуру кода и улучшая его читаемость.
# F, или "магический фильтр", позволяет "на лету" фильтровать входящие события и выдавать нужные результаты.
from aiogram import Router, F
# CommandStart срабатывает на команду /start,
# а Command активируется при любой команде, переданной аргументом.
from aiogram.filters import CommandStart, Command
# Мы также импортировали Message, чтобы использовать его для аннотации типов.
from aiogram.types import Message

start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    print(message)
    await message.answer('Запуск сообщения по команде /start используя фильтр CommandStart()')

@start_router.message(Command('start_2'))
async def cmd_start_2(message: Message):
    await message.answer('Запуск сообщения по команде /start_2 используя фильтр Command()')

@start_router.message(F.text == '/start_3')
async def cmd_start_3(message: Message):
    await message.answer('Запуск сообщения по команде /start_3 используя магический фильтр F.text!')