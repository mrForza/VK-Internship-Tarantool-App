from asynctnt import Connection
from fastapi import APIRouter, Depends, Request

from src.application.dto import (
    ReadKeyValuesRequestDto, ReadKeyValuesResponseDto, WriteKeyValuesRequestDto, WriteKeyValuesResponseDto
)
from src.application.services import KeyValueQueryService, KeyValueCommandService
from src.config import DbConfig
from src.presentation.api.providers.services import get_kv_query_service, get_kv_command_service

key_value_router = APIRouter(prefix='/api', tags=['key_value'])


@key_value_router.post('/read/', response_model=None)
async def read_key_value(
        request: Request,
        read_kv_dto: ReadKeyValuesRequestDto,
        kv_service: KeyValueQueryService = Depends(get_kv_query_service)
) -> ReadKeyValuesResponseDto:
    response = await kv_service.read_batch_of_keys(read_kv_dto, dict(request.headers))
    return response


@key_value_router.post('/write/', response_model=None)
async def write_key_value(
        request: Request,
        write_kv_dto: WriteKeyValuesRequestDto,
        kv_service: KeyValueCommandService = Depends(get_kv_command_service)
) -> WriteKeyValuesResponseDto:
    response = await kv_service.write_batch_of_key_values(write_kv_dto, dict(request.headers))
    return response
