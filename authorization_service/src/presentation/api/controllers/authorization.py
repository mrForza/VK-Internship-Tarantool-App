from fastapi import APIRouter, Depends, Request

from src.application.auth.dto import *
from src.application.auth.services import AuthorizationService
from src.presentation.api.providers.services import get_authorization_service

authorization_router = APIRouter(prefix='/auth', tags=['auth'])


@authorization_router.post('/register/', response_model=None)
async def register(
        registration_dto: RegistrationRequestDto,
        auth_service: AuthorizationService = Depends(get_authorization_service)
) -> RegistrationResponseDto:
    print('CONTROLLER authorization_router.register()')
    response = await auth_service.register(registration_dto)
    return response


@authorization_router.post('/login/', response_model=None)
async def authenticate(
        authentication_dto: AuthenticationRequestDto,
        auth_service: AuthorizationService = Depends(get_authorization_service)
) -> AuthenticationResponseDto:
    response = await auth_service.authenticate(authentication_dto)
    return response


@authorization_router.post('/logout/', response_model=None)
async def logout(
        requset: Request,
        auth_service: AuthorizationService = Depends(get_authorization_service)
) -> LogoutResponseDto:
    response = auth_service.logout(LogoutRequestDto(requset.headers.get('Authorization')))
    return response


@authorization_router.post('/check/', response_model=None)
def check(
        check_dto: CheckRequestDto,
        auth_service: AuthorizationService = Depends(get_authorization_service)
) -> CheckResponseDto:
    return auth_service.check(check_dto)
