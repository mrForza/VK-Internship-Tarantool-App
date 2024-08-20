from dataclasses import dataclass, field
from typing import List

from src.domain.common.entity import BaseEntity
from src.domain.value_objects.key import Key
from src.domain.exceptions import NoKeysInRequest, DublicatedKeys


class KeysValidator:
    @staticmethod
    def validate_quantity_of_keys(keys: 'Keys') -> None:
        if len(keys.value) == 0:
            raise NoKeysInRequest()

    @staticmethod
    def validate_duplicates(keys: 'Keys') -> None:
        occurrencies = {}
        for key in keys.value:
            occurrencies[key.value] = occurrencies.get(key.value, 0) + 1

        violated_keys = []
        for key, value in occurrencies.items():
            if value > 1:
                violated_keys.append(key)

        if len(violated_keys) > 0:
            raise DublicatedKeys(violated_keys)

    @staticmethod
    def validate_keys(keys: 'Keys'):
        KeysValidator.validate_quantity_of_keys(keys)
        KeysValidator.validate_duplicates(keys)


@dataclass
class Keys(BaseEntity):
    value: List[Key] = field(default_factory=list)
