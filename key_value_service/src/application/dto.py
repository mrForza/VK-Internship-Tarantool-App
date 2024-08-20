from dataclasses import asdict, dataclass
from typing import Any, Dict, List, Union


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
