from dataclasses import dataclass

from src.application.dto import (ReadKeyValuesRequestDto,
                                 ReadKeyValuesResponseDto,
                                 WriteKeyValuesRequestDto,
                                 WriteKeyValuesResponseDto)
from src.application.mapper import KeyValueMapper
from src.domain.entities.keys import KeysValidator
from src.infrastructure.db.repositories.kv_repository import KeyValueRepository
from src.infrastructure.external_api.auth_service import ExternalApiService


class GeneralKeyValueService:
    def rebalance_operations(self):
        pass


@dataclass
class KeyValueQueryService:
    general_service: GeneralKeyValueService
    kv_repository: KeyValueRepository
    external_api: ExternalApiService

    async def read_batch_of_keys(self, keys: ReadKeyValuesRequestDto, headers: dict) -> ReadKeyValuesResponseDto:
        self.external_api.check_authorization(headers)
        KeysValidator.validate_keys(KeyValueMapper.convert_keys_dto_to_entity(keys))  # check domain rules
        result = await self.kv_repository.read_key_values(keys.keys)
        return result


@dataclass
class KeyValueCommandService:
    general_service: GeneralKeyValueService
    kv_repository: KeyValueRepository
    external_api: ExternalApiService

    async def write_batch_of_key_values(
            self,
            key_values: WriteKeyValuesRequestDto,
            headers: dict
    ) -> WriteKeyValuesResponseDto:
        self.external_api.check_authorization(headers)
        KeysValidator.validate_keys(  # check domain rules
            KeyValueMapper.convert_keys_dto_to_entity(
                ReadKeyValuesRequestDto(list(key_values.data.keys()))
            )
        )
        return await self.kv_repository.write_key_values(key_values.data.items())
