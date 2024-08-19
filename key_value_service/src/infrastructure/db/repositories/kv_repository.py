from asynctnt import Connection, TarantoolTuple
from typing import List
from dataclasses import dataclass

from src.application.dto import WriteKeyValuesResponseDto, ReadKeyValuesResponseDto
from src.application.interfaces import KeyValueReader, KeyValueWriter
from src.infrastructure.db.common.repository import TarantoolRepositoy


@dataclass
class KeyValueRepository(TarantoolRepositoy, KeyValueReader, KeyValueWriter):
    conn: Connection

    async def read_key_values(self, keys: List[str]) -> ReadKeyValuesResponseDto:
        values = []
        for key in keys:
            try:
                tarantool_tuple: TarantoolTuple = (await self.conn.select('key_value_store', [key])).body[0]
                values.append(tarantool_tuple.get('value'))
            except Exception:
                continue
        await self.conn.disconnect()
        return ReadKeyValuesResponseDto({key: value for key, value in zip(keys, values)})

    async def write_key_values(self, key_values) -> WriteKeyValuesResponseDto:
        for key, value in key_values:
            try:
                await self.conn.insert('key_value_store', {'key': key, 'value': value})
            except Exception:
                continue
        await self.conn.disconnect()
        return WriteKeyValuesResponseDto('success')
