from typing import List, Dict, Any, Union
from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class ReadKeyValuesRequestDto:
    keys: List[Union[str, int, float]]
    dict = asdict


@dataclass(frozen=True)
class WriteKeyValuesRequestDto:
    data: Dict[Union[str, int, float], Any]
    dict = asdict


@dataclass(frozen=True)
class ReadKeyValuesResponseDto:
    data: Dict[Union[str, int, float], Any]
    dict = asdict


@dataclass(frozen=True)
class WriteKeyValuesResponseDto:
    status: str
    dict = asdict


@dataclass(frozen=True)
class ErrorResponse:
    message: str
    dict = asdict
