from dataclasses import dataclass
from typing import List, Union
from uuid import UUID


@dataclass(frozen=True)
class FullUserDto:
    login: str
    password: str
    name: str
    surname: str


@dataclass(frozen=True)
class ReducedUserDto:
    name: str
    surname: str


@dataclass(frozen=True)
class GetProfileResponseDto(ReducedUserDto):
    email: str
    user_id: UUID


@dataclass(frozen=True)
class GetAllUsersResponseDto:
    users: List[ReducedUserDto]
    total: int
    limit: Union[int, None]
    offset: Union[int, None]
