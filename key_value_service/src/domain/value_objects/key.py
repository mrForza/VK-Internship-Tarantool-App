from dataclasses import dataclass
from typing import Union, Any

from src.domain.common.value_object import BaseValueObject, BaseValueObjectValidator
from src.domain.exceptions import IncorrectTypeOfKey


class KeyValidator(BaseValueObjectValidator):
    def validate(self, raw_key: Any) -> None:
        if type(raw_key) not in (str, int, float):
            raise IncorrectTypeOfKey()


@dataclass(frozen=True)
class Key(BaseValueObject):
    value: Union[str, int, float]
    validator: KeyValidator = KeyValidator()
