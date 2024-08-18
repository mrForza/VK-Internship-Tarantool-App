from fastapi import APIRouter, Depends, Request

from src.application.dto import *
from src.application.services import KeyValueQueryService, KeyValueCommandService

key_value_router = APIRouter(prefix='/api', tags=['key_value'])


@key_value_router.get('/read/', response_model=None)
async def read_key_value(
        request: Request,
        read_kv_dto: ReadKeyValuesRequestDto,
        kv_service: KeyValueQueryService = Depends(KeyValueQueryService)
) -> ReadKeyValuesResponseDto:
    response = await kv_service.read_batch_of_keys(read_kv_dto)
    return response


@key_value_router.post('/write/', response_model=None)
async def write_key_value(
        request: Request,
        write_kv_dto: WriteKeyValuesRequestDto,
        kv_service: KeyValueCommandService = Depends(KeyValueCommandService)
) -> WriteKeyValuesResponseDto:
    response = await kv_service.write_batch_of_key_values(write_kv_dto)
    return response
