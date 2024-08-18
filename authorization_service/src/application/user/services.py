from passlib.context import CryptContext

from src.application.user.dto import FullUserDto
from src.application.user.mapper import UserMapper
from src.application.user.interfaces import UserReader, UserWriter
from src.application.auth.exceptions import UserAlreadyExists


class UserCommandService:
    def __init__(self, repo: UserWriter, mapper: UserMapper):
        self.repo = repo
        self.mapper = mapper

    async def save_user(self, user_dto: FullUserDto) -> None:
        user_entity = self.mapper.convert_full_user_dto_to_entity(user_dto)  # Check domain rules
        updated_dto = FullUserDto(
            user_dto.login,
            CryptContext(schemes=["bcrypt"], deprecated="auto").hash(user_dto.password, salt="a"*21 + "e"),
            user_dto.name,
            user_dto.surname
        )
        await self.repo.create_user(updated_dto)


class UserQueryService:
    def __init__(self, repo: UserReader):
        self.repo = repo

    async def check_user_existance(self, login: str) -> None:
        user = await self.repo.get_user_by_login(login)
        if user is not None:
            raise UserAlreadyExists()

    async def get_user(self, login: str) -> FullUserDto:
        user = await self.repo.get_user_by_login(login)
        if user is None:
            raise Exception()
        return user
