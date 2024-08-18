from dataclasses import dataclass

from src.domain.common.exception import DomainException
from src.domain.enums import ViolatedLength


@dataclass(frozen=True)
class LoginException(DomainException):
    @property
    def message(self) -> str:
        return 'Incorrect login'


@dataclass(frozen=True)
class BadLoginLength(LoginException):
    violation: ViolatedLength

    @property
    def message(self) -> str:
        return (
            f'{super().message}: the length should be no less than 2 symbols'
            if self.violation == ViolatedLength.SMALL else
            f'{super().message}: the length should be no more than 64 symbols'
        )


@dataclass(frozen=True)
class BadLoginContent(LoginException):
    @property
    def message(self) -> str:
        return f'{super().message}: login should have onlu lower-upper latin letters and digits'
