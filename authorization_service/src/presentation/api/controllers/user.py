from fastapi import APIRouter, Depends

from src.application.user.dto import UserDto, GetAllUsersResponseDto, GetProfileResponseDto
from src.application.user.services import UserQueryService

user_router = APIRouter(prefix='/users', tags=['user'])


@user_router.get('/')
def get_all_users(user_service: UserQueryService = Depends(UserQueryService)) -> GetAllUsersResponseDto:
    users = user_service.get_all_users()
    return users


@user_router.get('/{user_id}/')
def get_user_by_id(user_id: int, user_service: UserQueryService = Depends(UserQueryService)) -> UserDto:
    user = user_service.get_user_by_id(user_id)
    return user


@user_router.get('/{user_login}/')
def get_user_by_login(user_login: str, user_service: UserQueryService = Depends(UserQueryService)) -> UserDto:
    user = user_service.get_user_by_login(user_login)
    return user


@user_router.get('/me/')
def get_profile(user_service: UserQueryService = Depends(UserQueryService)) -> GetProfileResponseDto:
    profile = user_service.get_profile()
    return profile
