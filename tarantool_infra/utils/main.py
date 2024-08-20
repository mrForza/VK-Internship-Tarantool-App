import asyncio
from asynctnt import Connection


async def create_user(conn: Connection, login: str, password: str, name: str, surname: str) -> None:
    await conn.insert(
        'user',
        {
            'login': login,
            'password': password,
            'name': name,
            'surname': surname,
        }
    )
    await conn.disconnect()


async def main():
    conn = Connection(host='authorization_tarantool_db', port=3301)
    try:
        await conn.connect()
        user = await conn.select('user', ["admin"])
        if len(user.body) == 0:
            await create_user(
                conn,
                login='admin',
                password='$2b$12$aaaaaaaaaaaaaaaaaaaaaeju0Alh5lkuLd6gpN4VdpwmRnhoXHsCa',
                name='Admin',
                surname='Vkontaktovich'
            )
        print('Admin is already existed!')
        await conn.disconnect()
    except Exception:
        print('Something went wrong(')


if __name__ == '__main__':
    asyncio.run(main())
