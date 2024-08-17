from abc import ABC, ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import Any


class BaseValueObjectValidator(ABC):
    __meta__ = ABCMeta

    @abstractmethod
    def validate(self, *args, **kwargs) -> None:
        pass


@dataclass(frozen=True)
class BaseValueObject(ABC):
    value: Any
    validator: BaseValueObjectValidator

    def __post_init__(self) -> None:
        self.validator.validate(self.value)
