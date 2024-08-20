from dataclasses import dataclass

from src.domain.common.exception import DomainException
from src.domain.enums import MissingSymbols, ViolatedLength


@dataclass(frozen=True)
class PasswordException(DomainException):
    @property
    def message(self) -> str:
        return 'Incorrect password'


@dataclass(frozen=True)
class BadPasswordLength(PasswordException):
    violation: ViolatedLength

    @property
    def message(self) -> str:
        return (
            f'{super().message}: the length should be no less than 8 symbols'
            if self.violation == ViolatedLength.SMALL else
            f'{super().message}: the length should be no more than 64 symbols'
        )


@dataclass(frozen=True)
class BadPasswordContent(PasswordException):
    missing_symbols: MissingSymbols

    @property
    def message(self) -> str:
        return f'{super().message}: the password should have at least one {self.missing_symbols.name}'
