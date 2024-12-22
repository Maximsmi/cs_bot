# Импортируем библиотеку для логирования,
# чтобы записывать события и ошибки в процессе работы бота.
import logging
# Импортируем функцию config из библиотеки python-decouple
# для загрузки переменных окружения из файла .env.
from decouple import config
# Импортируем классы Bot и Dispatcher из библиотеки aiogram,
# которые необходимы для создания и управления ботом.
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
# Импортируем класс MemoryStorage для хранения состояний конечного автомата (FSM) в памяти.
from aiogram.fsm.storage.memory import MemoryStorage
# Импортируем класс AsyncIOScheduler из библиотеки APScheduler для планирования задач
# (например, выполнение скриптов по времени).
# from apscheduler.schedulers.asyncio import AsyncIOScheduler
#  Импортируем твой кастомный класс PostgresHandler для работы с базой данных Postgres
# from db_handler.db_class import PostgresHandler

# Создаем объект класса PostgresHandler для работы с базой данных.
# Строка подключения к базе данных загружается из переменной окружения PG_LINK.
# pg_db = PostgresHandler(config('PG_LINK'))

#scheduler = AsyncIOScheduler(timezone='Europe/Moscow')

# Создаем список ID администраторов бота.
# Загружаем строку с ID администраторов из переменной окружения ADMINS,
# разделяем её по запятым и преобразуем каждый элемент в целое число.
admins = [int(admin_id) for admin_id in config('ADMINS').split(',')]

# Настраиваем базовое логирование с уровнем INFO, чтобы записывать важные сообщения.
# Устанавливаем формат логов, включающий время, имя логгера и уровень сообщения.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# Создаем логгер с именем текущего модуля, чтобы записывать лог-сообщения.
logger = logging.getLogger(__name__)
formatter = logging.Formatter(
    "%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")

# Создаем объект Bot с токеном, загруженным из переменной окружения TOKEN.
bot = Bot(token=config("TOKEN"), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
# указывает, что для хранения состояния конечных автоматов (FSM) используется память (RAM).
# Это значит, что состояния пользователей будут храниться в оперативной памяти.
dp = Dispatcher(storage=MemoryStorage())