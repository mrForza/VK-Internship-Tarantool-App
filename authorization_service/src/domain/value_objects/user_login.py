from dataclasses import dataclass

from src.domain.common.value_object import BaseValueObject, BaseValueObjectValidator
from src.domain.exceptions.user_login import BadLoginLength, BadLoginContent, ViolatedLength


class UserLoginValidator(BaseValueObjectValidator):
    MINIMAL_LOGIN_LENGTH = 2

    MAXIMUM_LOGIN_LENGTH = 64

    AVAILABLE_SYMBOLS = set(
        '0123456789' +
        ''.join([chr(code) for code in range(97, 122 + 1)]) +
        ''.join([chr(code) for code in range(65, 90 + 1)])
    )
    
    def validate_length(self, raw_login: str) -> None:
        if len(raw_login) < self.MINIMAL_LOGIN_LENGTH:
            raise BadLoginLength(ViolatedLength.SMALL)
        elif len(raw_login) > self.MAXIMUM_LOGIN_LENGTH:
            raise BadLoginLength(ViolatedLength.BIG)

    def validate_symbols(self, raw_login: str):
        login_unique_symbols = set(raw_login)
        if login_unique_symbols.difference(self.AVAILABLE_SYMBOLS):
            raise BadLoginContent()
    
    def validate(self, raw_login: str) -> None:
        self.validate_length(raw_login)
        self.validate_symbols(raw_login)


@dataclass(frozen=True)
class UserLogin(BaseValueObject):
    value: str
    validator: UserLoginValidator = UserLoginValidator()
