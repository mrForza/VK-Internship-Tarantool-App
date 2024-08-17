from dataclasses import dataclass

from src.domain.common.aggregate_root import AggregateRoot
from src.domain.value_objects import *


@dataclass()
class User(AggregateRoot):
    login: UserLogin
    password: UserPassword
    name: UserName
    surname: UserSurName
