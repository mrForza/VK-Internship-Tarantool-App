from dataclasses import dataclass
from typing import List, Union


@dataclass(frozen=True)
class ApplicationException(Exception):
    @property
    def message(self) -> str:
        return 'An error occured in application layer. Some UseCases have been violated!'


@dataclass(frozen=True)
class UserIsNotAuthorized(ApplicationException):
    @property
    def message(self) -> str:
        return 'You are not authorized! Please, sign in or sign up'


@dataclass(frozen=True)
class KeysDoNotExist(ApplicationException):
    not_existing_keys: List[Union[str, int, float]]

    @property
    def message(self) -> str:
        representation = ' '.join(self.not_existing_keys)
        return f'These keys don\'t exist: {representation}'


DEFAULT_ERROR_MESSAGE = 'Oops, something went wrong! Maybe a computer virus destroys our app)'
