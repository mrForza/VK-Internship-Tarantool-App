class ApplicationException(Exception):
    @property
    def message(self) -> str:
        return 'An error occured in application layer. Some UseCases have been violated!'


class UserAlreadyExists(ApplicationException):
    @property
    def message(self) -> str:
        return 'A user with this login is already exists'


class MismatchedPasswords(ApplicationException):
    @property
    def message(self) -> str:
        return 'You have entered an incorrect password('
