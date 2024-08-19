from dataclasses import dataclass
from typing import List, Union

from src.application.dto import *
from src.application.exceptions import ApplicationException, DublicatedKeys
from src.infrastructure.db.repositories.kv_repository import KeyValueRepository
from src.infrastructure.external_api.auth_service import ExternalApiService


class GeneralKeyValueService:
    def validate_keys(self, keys: List[Union[str, int, float]]):
        occurrencies = {}
        for key in keys:
            occurrencies[key] = occurrencies.get(key, 0) + 1

        violated_keys = []
        for key, value in occurrencies.items():
            if value > 1:
                violated_keys.append(key)

        if len(violated_keys) > 0:
            raise DublicatedKeys(violated_keys)

    def rebalance_operations(self):
        pass


@dataclass
class KeyValueQueryService:
    general_service: GeneralKeyValueService
    kv_repository: KeyValueRepository
    external_api: ExternalApiService

    async def read_batch_of_keys(self, keys: ReadKeyValuesRequestDto, headers: dict) -> ReadKeyValuesResponseDto:
        try:
            self.external_api.check_authorization(headers)
            unique_keys = list(set(keys.keys))
            result = await self.kv_repository.read_key_values(unique_keys)
            return result
        except Exception as error:
            print(error)
            return ReadKeyValuesResponseDto(data={'-': '-'})


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
        try:
            self.external_api.check_authorization(headers)
            self.general_service.validate_keys(list(key_values.data.keys()))
            await self.kv_repository.write_key_values(key_values.data.items())
            return WriteKeyValuesResponseDto('success')
        except ApplicationException as error:
            return WriteKeyValuesResponseDto(error.message)
        except Exception as error:
            print(error)
            return WriteKeyValuesResponseDto('Something went wrong')
