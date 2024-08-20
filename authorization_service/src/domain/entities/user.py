from dataclasses import dataclass

from src.domain.common.aggregate_root import AggregateRoot
from src.domain.value_objects.user_initials import UserName, UserSurName
from src.domain.value_objects.user_login import UserLogin
from src.domain.value_objects.user_password import UserPassword


@dataclass()
class User(AggregateRoot):
    login: UserLogin
    password: UserPassword
    name: UserName
    surname: UserSurName
