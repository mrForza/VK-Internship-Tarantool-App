from typing import List, Dict, Any, Union


class ReadKeyValuesRequestDto:
    keys: List[Union[str, int, float]]


class WriteKeyValuesRequestDto:
    data: Dict[Union[str, int, float], Any]


class ReadKeyValuesResponseDto:
    data: Dict[Union[str, int, float], Any]


class WriteKeyValuesResponseDto:
    status: str
