from fastapi import Depends

from src.application.services import (GeneralKeyValueService,
                                      KeyValueCommandService,
                                      KeyValueQueryService)
from src.infrastructure.db.main import get_connection
from src.infrastructure.db.repositories.kv_repository import KeyValueRepository
from src.infrastructure.external_api.auth_service import ExternalApiService


def get_external_api_service() -> ExternalApiService:
    return ExternalApiService()


def get_kv_general_service() -> GeneralKeyValueService:
    return GeneralKeyValueService()


async def get_kv_repository() -> KeyValueRepository:
    conn = await get_connection()
    return KeyValueRepository(conn)


async def get_kv_command_service(
        general_service: GeneralKeyValueService = Depends(get_kv_general_service),
        kv_repository: KeyValueRepository = Depends(get_kv_repository),
        external_api: ExternalApiService = Depends(get_external_api_service)
) -> KeyValueCommandService:
    return KeyValueCommandService(general_service, kv_repository, external_api)


async def get_kv_query_service(
        general_service: GeneralKeyValueService = Depends(get_kv_general_service),
        kv_repository: KeyValueRepository = Depends(get_kv_repository),
        external_api: ExternalApiService = Depends(get_external_api_service)
) -> KeyValueQueryService:
    return KeyValueQueryService(general_service, kv_repository, external_api)
