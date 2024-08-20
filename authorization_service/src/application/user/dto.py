from dataclasses import asdict, dataclass
from typing import List
from uuid import UUID


@dataclass(frozen=True)
class FullUserDto:
    login: str
    password: str
    name: str
    surname: str
    dict = asdict


@dataclass(frozen=True)
class ReducedUserDto:
    name: str
    surname: str
    dict = asdict


@dataclass(frozen=True)
class GetProfileResponseDto(ReducedUserDto):
    email: str
    user_id: UUID
    dict = asdict


@dataclass(frozen=True)
class GetAllUsersResponseDto:
    users: List[ReducedUserDto]
    dict = asdict
