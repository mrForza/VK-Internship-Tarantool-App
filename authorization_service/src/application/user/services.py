from uuid import uuid4

from src.application.user.dto import UserDto, GetAllUsersResponseDto, GetProfileResponseDto


class UserCommandService:
    pass


class UserQueryService:
    def get_user_by_id(self, user_id: int) -> UserDto:
        return UserDto('Roman', 'Gromov')

    def get_user_by_login(self, login: str) -> UserDto:
        return UserDto('Roman', 'Gromov')

    def get_all_users(self) -> GetAllUsersResponseDto:
        return GetAllUsersResponseDto(
            users=[UserDto('Roman', 'Gromov'), UserDto('Kirill', 'Sarychev')],
            total=2,
            limit=2,
            offset=0
        )

    def get_profile(self) -> GetProfileResponseDto:
        return GetProfileResponseDto('Roman', 'Gromov', 'rsgromov@edu.hse.ru', uuid4())
