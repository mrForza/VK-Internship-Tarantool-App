from dataclasses import dataclass

from src.domain.common.value_object import (BaseValueObject,
                                            BaseValueObjectValidator)
from src.domain.exceptions.user_password import (BadPasswordContent,
                                                 BadPasswordLength,
                                                 MissingSymbols,
                                                 ViolatedLength)


class UserPasswordValidator(BaseValueObjectValidator):
    MINIMAL_PASSWORD_LENGTH = 8

    MAXIMUM_PASSWORD_LENGTH = 64

    SPECIAL_SYMBOLS = set('!@#$%^&*()_+-=/.,')

    LOWERCASE_LETTERS = set([chr(code) for code in range(97, 122 + 1)])

    UPPERCASE_LETTERS = set([chr(code) for code in range(65, 90 + 1)])

    DIGITS = set('0123456789')

    def validate_length(self, raw_password: str) -> None:
        if len(raw_password) < self.MINIMAL_PASSWORD_LENGTH:
            raise BadPasswordLength(ViolatedLength.SMALL)
        elif len(raw_password) > self.MAXIMUM_PASSWORD_LENGTH:
            raise BadPasswordLength(ViolatedLength.BIG)

    def validate_symbols(self, raw_password: str) -> None:
        unique_symbols = set(raw_password)

        for i, symbols_set in enumerate([
                self.LOWERCASE_LETTERS,
                self.UPPERCASE_LETTERS,
                self.DIGITS,
                self.SPECIAL_SYMBOLS
        ]):
            if not unique_symbols.intersection(symbols_set):
                raise BadPasswordContent(MissingSymbols(i))

    def validate(self, raw_password: str) -> None:
        self.validate_length(raw_password)
        self.validate_symbols(raw_password)

    def __repr__(self):
        return 'UserPasswordValidator'


@dataclass(frozen=True)
class UserPassword(BaseValueObject):
    value: str
    validator: UserPasswordValidator = UserPasswordValidator()
