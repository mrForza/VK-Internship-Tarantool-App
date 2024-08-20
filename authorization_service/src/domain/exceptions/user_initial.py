from dataclasses import dataclass

from src.domain.common.exception import DomainException
from src.domain.enums import ViolatedLength


@dataclass(frozen=True)
class InitialException(DomainException):
    @property
    def message(self) -> str:
        return 'Incorrect initial'


@dataclass(frozen=True)
class BadInitialLength(InitialException):
    violation: ViolatedLength

    @property
    def message(self) -> str:
        return (
            f'{super().message}: the length should be no less than 2 symbols'
            if self.violation == ViolatedLength.SMALL else
            f'{super().message}: the length should be no more than 32 symbols'
        )


@dataclass(frozen=True)
class BadInitialContent(InitialException):
    @property
    def message(self) -> str:
        return f'{super().message}: initial should have only lower-upper latin letters'
