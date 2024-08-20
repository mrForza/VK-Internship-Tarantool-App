from functools import wraps

from fastapi import APIRouter, Depends, Request
from starlette.responses import JSONResponse

from src.application.dto import (ErrorResponse, ReadKeyValuesRequestDto,
                                 ReadKeyValuesResponseDto,
                                 WriteKeyValuesRequestDto,
                                 WriteKeyValuesResponseDto)
from src.application.exceptions import (DEFAULT_ERROR_MESSAGE,
                                        ApplicationException,
                                        UserIsNotAuthorized)
from src.application.services import (KeyValueCommandService,
                                      KeyValueQueryService)
from src.domain.common.exception import DomainException
from src.presentation.api.providers.services import (get_kv_command_service,
                                                     get_kv_query_service)

key_value_router = APIRouter(prefix='/api', tags=['key_value'])


def exception_handler(dto_class):
    def additional_wrapper(inner_func):
        @wraps(inner_func)
        async def wrapper(*args, **kwargs):
            try:
                result = await inner_func(*args, **kwargs)
                return result
            except UserIsNotAuthorized as error:
                return JSONResponse(content=ErrorResponse(error.message).dict(), status_code=401)
            except (ApplicationException, DomainException) as error:
                return JSONResponse(content=ErrorResponse(error.message).dict(), status_code=400)
            except Exception as error:
                print(error)
                return JSONResponse(content=ErrorResponse(DEFAULT_ERROR_MESSAGE).dict(), status_code=418)
        return wrapper
    return additional_wrapper


@key_value_router.post('/read/', response_model=None)
@exception_handler(dto_class=ReadKeyValuesResponseDto)
async def read_key_value(
        request: Request,
        read_kv_dto: ReadKeyValuesRequestDto,
        kv_service: KeyValueQueryService = Depends(get_kv_query_service)
) -> JSONResponse:
    response = await kv_service.read_batch_of_keys(read_kv_dto, dict(request.headers))
    return JSONResponse(content=response.dict(), status_code=200)


@key_value_router.post('/write/', response_model=None)
@exception_handler(dto_class=WriteKeyValuesResponseDto)
async def write_key_value(
        request: Request,
        write_kv_dto: WriteKeyValuesRequestDto,
        kv_service: KeyValueCommandService = Depends(get_kv_command_service)
) -> JSONResponse:
    response = await kv_service.write_batch_of_key_values(write_kv_dto, dict(request.headers))
    return JSONResponse(content=response.dict(), status_code=201)
