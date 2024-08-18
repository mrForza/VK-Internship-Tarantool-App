from fastapi import APIRouter, Depends

from src.application.user.services import UserQueryService

user_router = APIRouter(prefix='/users', tags=['user'])

#
# @user_router.get('/', response_model=None)
# def get_all_users(user_service: UserQueryService = Depends(UserQueryService)) -> str:#GetAllUsersResponseDto:
#     # users = user_service.get_all_users()
#     return ''
#
#
# @user_router.get('/{user_id}/', response_model=None)
# def get_user_by_id(user_id: int, user_service: UserQueryService = Depends(UserQueryService)) -> str:#UserDto:
#     # user = user_service.get_user_by_id(user_id)
#     return ''
#
#
# @user_router.get('/{user_login}/', response_model=None)
# def get_user_by_login(user_login: str, user_service: UserQueryService = Depends(UserQueryService)) -> str: #UserDto:
#     # user = user_service.get_user_by_login(user_login)
#     return ''
#
#
# @user_router.get('/me/', response_model=None)
# def get_profile(user_service: UserQueryService = Depends(UserQueryService)) -> str:#GetProfileResponseDto:
#     # profile = user_service.get_profile()
#     return ''
