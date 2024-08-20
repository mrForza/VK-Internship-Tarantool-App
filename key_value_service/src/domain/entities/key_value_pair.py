from dataclasses import dataclass

from src.domain.value_objects.key import Key
from src.domain.value_objects.value import Value
from src.domain.common.entity import BaseEntity


@dataclass
class KeyValuePair(BaseEntity):
    key: Key
    value: Value
