from dataclasses import dataclass
from typing import List, Union

from src.domain.common.exception import DomainException


@dataclass(frozen=True)
class KeyExceptiom(DomainException):
    @property
    def message(self) -> str:
        return 'Incorrect key'


@dataclass(frozen=True)
class IncorrectTypeOfKey(KeyExceptiom):
    @property
    def message(self) -> str:
        return f'{super().message}: the type of key should be: str, int or float'


@dataclass(frozen=True)
class DublicatedKeys(KeyExceptiom):
    duplicated_keys: List[Union[str, int, float]]

    @property
    def message(self) -> str:
        representation = ' '.join(self.duplicated_keys)
        return f'Incorrect keys: you cannot pass identical keys: {representation}'


@dataclass(frozen=True)
class NoKeysInRequest(KeyExceptiom):
    @property
    def message(self) -> str:
        return f'Incorrect keys: you have not passed any keys'
