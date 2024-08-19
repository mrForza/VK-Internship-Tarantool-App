from dataclasses import dataclass
from typing import List, Union


@dataclass(frozen=True)
class ApplicationException(Exception):
    @property
    def message(self) -> str:
        return 'An error occured in application layer. Some UseCases have been violated!'


@dataclass(frozen=True)
class DublicatedKeys(ApplicationException):
    duplicated_keys: List[Union[str, int, float]]

    @property
    def message(self) -> str:
        representation = ' '.join(self.duplicated_keys)
        return f'Incorrect keys! You cannot write identical keys: {representation}'


@dataclass(frozen=True)
class UserIsNotAuthorized(ApplicationException):
    @property
    def message(self) -> str:
        return 'You are not authorized! Please, sign in or sign up'
