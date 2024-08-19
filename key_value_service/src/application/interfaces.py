from abc import ABC, abstractmethod
from typing import List

from src.application.dto import ReadKeyValuesResponseDto, WriteKeyValuesResponseDto


class KeyValueReader(ABC):
    @abstractmethod
    async def read_key_values(self, keys: List[str]) -> ReadKeyValuesResponseDto:
        pass


class KeyValueWriter(ABC):
    @abstractmethod
    async def write_key_values(self, key_values) -> WriteKeyValuesResponseDto:
        pass
