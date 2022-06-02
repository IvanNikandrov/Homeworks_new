"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
from models import create_tables, save_user_and_post_in_db
from jsonplaceholder_requests import fetch_json, USERS_DATA_URL, POSTS_DATA_URL


async def async_main():
    await create_tables()
    user_data, post_data = await asyncio.gather(fetch_json(USERS_DATA_URL), fetch_json(POSTS_DATA_URL))
    await save_user_and_post_in_db(user_data, post_data)



def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
