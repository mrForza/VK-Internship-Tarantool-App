from typing import List, Union
from dataclasses import dataclass

from asynctnt import Connection

from src.application.user.dto import FullUserDto
from src.infrastructure.db.common.repository import TarantoolRepositoy
from src.application.user.interfaces import UserReader, UserWriter


@dataclass
class UserRepository(TarantoolRepositoy, UserReader, UserWriter):
    conn: Connection

    async def get_user_by_id(self, user_id: int) -> Union[FullUserDto, None]:
        result = await self.conn.select('user', [user_id])
        if len(result.body) == 0:
            return None
        user = result.body[0]
        await self.conn.disconnect()
        return FullUserDto(
            user.get('login'),
            user.get('password'),
            user.get('name'),
            user.get('surname')
        )

    async def get_user_by_login(self, login: str) -> Union[FullUserDto, None]:
        result = await self.conn.select('user', [login])
        if len(result.body) == 0:
            return None
        user = result.body[0]
        await self.conn.disconnect()
        return FullUserDto(
            user.get('login'),
            user.get('password'),
            user.get('name'),
            user.get('surname')
        )

    async def get_all_users(self) -> List[FullUserDto]:
        users = (await self.conn.select('users', [])).body
        await self.conn.disconnect()
        return users

    async def create_user(self, user_dto: FullUserDto) -> None:
        await self.conn.insert(
            'user',
            {
                'login': user_dto.login,
                'password': user_dto.password,
                'name': user_dto.name,
                'surname': user_dto.surname,
            }
        )
        await self.conn.disconnect()
