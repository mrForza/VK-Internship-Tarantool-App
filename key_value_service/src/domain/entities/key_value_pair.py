from dataclasses import dataclass

from src.domain.value_objects.key import Key
from src.domain.value_objects.value import Value
from src.domain.common.aggregate_root import AggregateRoot


@dataclass
class KeyValuePair(AggregateRoot):
    key: Key
    value: Value
