from enum import Enum
from dataclasses import dataclass

from src.domain.common.value_object import BaseValueObject, BaseValueObjectValidator


class TypeOfInitial(int, Enum):
    NAME = 0,
    SURNAME = 1,


class UserInitialValidator(BaseValueObjectValidator):
    MIN_NAME_LENGTH = 2

    MAX_NAME_LENGTH = 32

    def validate_length(self, raw_initial: str, type_of_initial=None) -> None:
        if len(raw_initial) < self.MIN_NAME_LENGTH:
            raise Exception()
        elif len(raw_initial) > self.MAX_NAME_LENGTH:
            raise Exception()

    def validate_symbols(self, raw_initial: str, type_of_initial=None) -> None:
        if raw_initial.count('-') == len(raw_initial):
            raise Exception()

        for symbol in raw_initial:
            if symbol != '-' and (ord(symbol) < 65 or 90 < ord(symbol) < 97 or ord(symbol) > 122):
                raise Exception()

    def validate(self, raw_initial: str) -> None:
        self.validate_length(raw_initial)
        self.validate_symbols(raw_initial)

    def __repr__(self) -> str:
        return 'UserInitialValidator'


@dataclass(frozen=True)
class UserInitial(BaseValueObject):
    value: str
    validator: UserInitialValidator = UserInitialValidator()


class UserName(UserInitial):
    pass


class UserSurName(UserInitial):
    pass
