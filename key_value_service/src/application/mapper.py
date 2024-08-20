from typing import Union, Any

from src.application.dto import *
from src.domain.value_objects.key import Key
from src.domain.value_objects.value import Value
from src.domain.entities.keys import Keys


class KeyValueMapper:
    @staticmethod
    def convert_key_to_value_object(key: Union[str, int, float]) -> Key:
        return Key(key)

    @staticmethod
    def convert_value_to_value_object(value: Any) -> Value:
        return Value(value)

    @staticmethod
    def convert_keys_dto_to_entity(keys_dto: ReadKeyValuesRequestDto) -> Keys:
        data = [KeyValueMapper.convert_key_to_value_object(key) for key in keys_dto.keys]
        return Keys(data)
