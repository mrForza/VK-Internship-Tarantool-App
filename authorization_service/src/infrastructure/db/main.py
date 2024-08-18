from asynctnt import Connection

from src.config import DbConfig


async def get_connection() -> Connection:
    conn = Connection(host=DbConfig().host, port=DbConfig().port)
    await conn.connect()
    print('Let\'s start!')
    return conn
