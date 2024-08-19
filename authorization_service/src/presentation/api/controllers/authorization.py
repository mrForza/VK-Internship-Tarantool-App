from dataclasses import asdict
from functools import wraps

from fastapi import APIRouter, Depends, Request
from starlette.responses import JSONResponse

from src.application.auth.dto import *
from src.application.auth.services import AuthorizationService
from src.application.auth.exceptions import ApplicationException, UserIsNotAuthorized, DEFAUL_ERROR_MESSAGE
from src.presentation.api.providers.services import get_authorization_service
from src.domain.common.exception import DomainException

authorization_router = APIRouter(prefix='/auth', tags=['auth'])


def exception_handler(dto_class):
    def additional_wrapper(inner_func):
        @wraps(inner_func)
        async def wrapper(*args, **kwargs):
            try:
                result = await inner_func(*args, **kwargs)
                return result
            except UserIsNotAuthorized as error:
                return JSONResponse(content=dto_class(error.message).dict(), status_code=401)
            except (ApplicationException, DomainException) as error:
                return JSONResponse(content=dto_class(error.message).dict(), status_code=400)
            except Exception:
                print('1' * 100)
                return JSONResponse(content=dto_class(DEFAUL_ERROR_MESSAGE).dict(), status_code=418)
        return wrapper
    return additional_wrapper


@authorization_router.post('/register/', response_model=None)
@exception_handler(dto_class=RegistrationResponseDto)
async def register(
        registration_dto: RegistrationRequestDto,
        auth_service: AuthorizationService = Depends(get_authorization_service),
) -> JSONResponse:
    response = await auth_service.register(registration_dto)
    return JSONResponse(content=response.dict(), status_code=201)


@authorization_router.post('/login/', response_model=None)
@exception_handler(dto_class=LogoutResponseDto)
async def authenticate(
        authentication_dto: AuthenticationRequestDto,
        auth_service: AuthorizationService = Depends(get_authorization_service)
) -> JSONResponse:
    response = await auth_service.authenticate(authentication_dto)
    return JSONResponse(content=response.dict(), status_code=201)


@authorization_router.post('/logout/', response_model=None)
@exception_handler(dto_class=LogoutResponseDto)
async def logout(
        requset: Request,
        auth_service: AuthorizationService = Depends(get_authorization_service)
) -> JSONResponse:
    response = auth_service.logout(LogoutRequestDto(requset.headers.get('Authorization')))
    return JSONResponse(content=response.dict(), status_code=201)


@authorization_router.post('/check/', response_model=None)
def check(
        check_dto: CheckRequestDto,
        auth_service: AuthorizationService = Depends(get_authorization_service)
) -> JSONResponse:
    response = auth_service.check(check_dto)
    return JSONResponse(content=response.dict(), status_code=200)
