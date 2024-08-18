from abc import ABC, abstractmethod
from typing import List, Union

from src.application.user.dto import FullUserDto


class UserReader(ABC):
    @abstractmethod
    async def get_user_by_id(self, user_id: int) -> Union[FullUserDto, None]:
        pass

    @abstractmethod
    async def get_user_by_login(self, login: str) -> Union[FullUserDto, None]:
        pass

    @abstractmethod
    async def get_all_users(self) -> List[FullUserDto]:
        pass


class UserWriter(ABC):
    @abstractmethod
    async def create_user(self, user_dto: FullUserDto) -> None:
        pass
