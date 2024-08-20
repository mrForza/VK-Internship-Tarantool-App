from asynctnt import Connection, TarantoolTuple
from typing import List
from dataclasses import dataclass

from src.application.dto import WriteKeyValuesResponseDto, ReadKeyValuesResponseDto
from src.application.exceptions import KeysDoNotExist
from src.application.interfaces import KeyValueReader, KeyValueWriter
from src.infrastructure.db.common.repository import TarantoolRepositoy


@dataclass
class KeyValueRepository(TarantoolRepositoy, KeyValueReader, KeyValueWriter):
    conn: Connection

    async def read_key_values(self, keys: List[str]) -> ReadKeyValuesResponseDto:
        values = []
        not_existing_keys = []
        for key in keys:
            try:
                tarantool_tuple: TarantoolTuple = (await self.conn.select('key_value_store', [key])).body[0]
                values.append(tarantool_tuple.get('value'))
            except Exception:
                not_existing_keys.append(key)
        await self.conn.disconnect()
        if len(not_existing_keys) > 0:
            raise KeysDoNotExist(not_existing_keys)
        return ReadKeyValuesResponseDto({key: value for key, value in zip(keys, values)})

    async def write_key_values(self, key_values) -> WriteKeyValuesResponseDto:
        existing_keys = []
        warning = ''
        for key, value in key_values:
            try:
                await self.conn.insert('key_value_store', {'key': key, 'value': value})
            except Exception:
                existing_keys.append(key)
        await self.conn.disconnect()
        if len(existing_keys) > 0:
            warning = f', but these keys have not been written: {" ".join(existing_keys)}. ' \
                      f'Because they have already been in kv store'
        return WriteKeyValuesResponseDto(f'success{warning}')
