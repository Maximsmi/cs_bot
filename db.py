# Импортируем функцию config из библиотеки python-decouple
# для загрузки переменных окружения из файла .env.
from decouple import config

import asyncio
import asyncpg


# Установите соединение с существующей базой данных с именем
# от имени пользователя.
# conn = await asyncpg.connect('postgresql://postgres@localhost/test')
async def connect_db():
    conn = await asyncpg.connect(config('PG_LINK'))
    # Проверяем есть ли таблица в базе данных, если нет, то создаем
    # Таблица со списком пользователей которые подключились к боту
    # id - автоматический инкремент
    # date_conn - дата присоединения к боту
    # id_user - id пользователя в телеграмме
    # first_name - Имя пользователя
    # last_name - Фамилия пользователя
    # username - никнайм пользователя
    #
    await conn.execute('''CREATE TABLE users_con(   id serial PRIMARY KEY,
                                                    date_conn TEXT,
                                                    id_user TEXT,
                                                    first_name TEXT,
                                                    last_name TEXT,
                                                    username TEXT
                                                )
                        ''')

    # Таблица со списком номенклатуры товара
    # id - автоматический инкремент
    # name_item - дата присоединения к боту
    # id_user - id пользователя в телеграмме
    # first_name - Имя пользователя
    # last_name - Фамилия пользователя
    # username - никнайм пользователя
    #
    await conn.execute('''CREATE TABLE users_con(   id serial PRIMARY KEY,
                                                    date_conn TEXT,
                                                    id_user TEXT,
                                                    first_name TEXT,
                                                    last_name TEXT,
                                                    username TEXT
                                                )
                        ''')

async def main():
    # Establish a connection to an existing database named "test"
    # as a "postgres" user.
    conn = await asyncpg.connect('postgresql://postgres@localhost/test')
    # Execute a statement to create a new table.


    # Insert a record into the created table.
    await conn.execute('''
 INSERT INTO users(name, dob) VALUES($1, $2)
 ''', 'Bob', datetime.date(1984, 3, 1))

    # Select a row from the table.
    row = await conn.fetchrow(
        'SELECT * FROM users WHERE name = $1', 'Bob')
    # *row* now contains
    # asyncpg.Record(id=1, name='Bob', dob=datetime.date(1984, 3, 1))

    # Close the connection.
    await conn.close()

asyncio.run(main())
async def run():
    conn = await asyncpg.connect(user='user', password='password',
                                 database='database', host='127.0.0.1')
    values = await conn.fetch('''SELECT * FROM mytable''')
    await conn.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(run())