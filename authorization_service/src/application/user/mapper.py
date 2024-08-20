from src.domain.entities.user import User
from src.domain.value_objects import (
    UserLogin, UserPassword, UserName, UserSurName
)
from src.application.user.dto import FullUserDto
from src.application.auth.dto import RegistrationRequestDto


class UserMapper:
    @staticmethod
    def convert_entity_to_full_user_dto(entity: User) -> FullUserDto:
        return FullUserDto(
            name=entity.name.value,
            surname=entity.surname.value,
            login=entity.login.value,
            password=entity.password.value
        )

    @staticmethod
    def convert_full_user_dto_to_entity(dto: FullUserDto) -> User:
        return User(
            login=UserLogin(dto.login),
            password=UserPassword(dto.password),
            name=UserName(dto.name),
            surname=UserSurName(dto.surname)
        )

    @staticmethod
    def convert_registration_dto_to_full_user_dto(registration_dto: RegistrationRequestDto) -> FullUserDto:
        return FullUserDto(
            name=registration_dto.name,
            surname=registration_dto.surname,
            login=registration_dto.login,
            password=registration_dto.password
        )
