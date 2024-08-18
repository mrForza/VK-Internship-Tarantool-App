from dataclasses import dataclass

from src.domain.common.exception import DomainException


@dataclass(frozen=True)
class KeyExceptiom(DomainException):
    @property
    def message(self) -> str:
        return 'Incorrect key'


@dataclass(frozen=True)
class IncorrectTypeOfKey(DomainException):
    @property
    def message(self) -> str:
        return f'{super().message}: the type of key should be: str, int or float'
