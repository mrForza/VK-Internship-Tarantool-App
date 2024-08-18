from dataclasses import dataclass
from typing import List, Union

from src.application.dto import *


class GeneralKeyValueService:
    def validate_keys(self, keys: List[Union[str, int, float]]):
        occurrencies = {}
        for key in keys:
            occurrencies[key] = occurrencies.get(key, 0) + 1

        violated_keys = []
        for key, value in occurrencies.items():
            if value > 1:
                violated_keys.append(key)

        raise Exception('')

    def rebalance_operations(self):
        pass


@dataclass
class KeyValueQueryService:
    general_service: GeneralKeyValueService

    async def read_batch_of_keys(self, keys: ReadKeyValuesRequestDto) -> ReadKeyValuesResponseDto:
        pass


@dataclass
class KeyValueCommandService:
    general_service: GeneralKeyValueService

    async def write_batch_of_key_values(self, key_values: WriteKeyValuesRequestDto) -> WriteKeyValuesResponseDto:
        pass
