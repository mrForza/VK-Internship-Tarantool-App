import asynctnt
import tarantool

from src.config import DbConfig


async def init_connection(db_config: DbConfig):
    conn = asynctnt.Connection(host=db_config.host, port=db_config.port)
    await conn.connect()
    print('!' * 30, 'OK')
