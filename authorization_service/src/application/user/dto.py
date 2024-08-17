from dataclasses import dataclass
from typing import List, Union
from uuid import UUID


@dataclass(frozen=True)
class UserDto:
    name: str
    surname: str


@dataclass(frozen=True)
class GetProfileResponseDto(UserDto):
    email: str
    user_id: UUID


@dataclass(frozen=True)
class GetAllUsersResponseDto:
    users: List[UserDto]
    total: int
    limit: Union[int, None]
    offset: Union[int, None]
