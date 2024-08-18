from dataclasses import dataclass
from typing import Any

from src.domain.common.value_object import BaseValueObject, BaseValueObjectValidator


class ValueValidator(BaseValueObjectValidator):
    def validate(self, raw_value: Any) -> None:
        pass


@dataclass(frozen=True)
class Value(BaseValueObject):
    value: Any
    validator: ValueValidator = ValueValidator()
