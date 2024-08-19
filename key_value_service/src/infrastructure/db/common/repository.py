from abc import ABC
from typing import Any

from asynctnt import Connection


class BaseRepository(ABC):
    def __init__(self, mapper: Any) -> None:
        self.mapper = mapper


class TarantoolRepositoy(BaseRepository):
    def __init__(self, mapper: Any, connection: Connection) -> None:
        self.connection = connection
        super().__init__(mapper)
