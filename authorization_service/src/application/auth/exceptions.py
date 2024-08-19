from dataclasses import dataclass


@dataclass(frozen=True)
class ApplicationException(Exception):
    @property
    def message(self) -> str:
        return 'An error occured in application layer. Some UseCases have been violated!'


@dataclass(frozen=True)
class UserAlreadyExists(ApplicationException):
    @property
    def message(self) -> str:
        return 'A user with this login is already exists'


@dataclass(frozen=True)
class UserIsNotAuthorized(ApplicationException):
    @property
    def message(self) -> str:
        return 'You have not been authorized!'


@dataclass(frozen=True)
class IncorrectLoginOrPassword(ApplicationException):
    @property
    def message(self) -> str:
        return 'You have entered an incorrect login or password'


@dataclass(frozen=True)
class MismatchedPasswords(ApplicationException):
    @property
    def message(self) -> str:
        return 'You have entered an incorrect password('


DEFAUL_ERROR_MESSAGE = 'Something went wrong! Please, check your databases and services'
