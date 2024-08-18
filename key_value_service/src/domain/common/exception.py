from dataclasses import dataclass


@dataclass(frozen=True)
class DomainException(Exception):
    @property
    def message(self) -> str:
        return 'An error occured in domain layer of application. Some business rules have been violated!'
