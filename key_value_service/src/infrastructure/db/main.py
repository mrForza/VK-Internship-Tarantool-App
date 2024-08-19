from asynctnt import Connection

from src.config import DbConfig

db_config = DbConfig()


async def get_connection() -> Connection:
    connection = Connection(host=db_config.host, port=db_config.port)
    await connection.connect()
    return connection