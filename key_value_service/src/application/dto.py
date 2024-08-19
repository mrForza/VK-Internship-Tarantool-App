from typing import List, Dict, Any, Union
from dataclasses import dataclass


@dataclass(frozen=True)
class ReadKeyValuesRequestDto:
    keys: List[Union[str, int, float]]


@dataclass(frozen=True)
class WriteKeyValuesRequestDto:
    data: Dict[Union[str, int, float], Any]


@dataclass(frozen=True)
class ReadKeyValuesResponseDto:
    data: Dict[Union[str, int, float], Any]


@dataclass(frozen=True)
class WriteKeyValuesResponseDto:
    status: str
