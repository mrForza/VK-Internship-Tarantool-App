import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext

from src.application.user.services import UserQueryService, UserCommandService
from src.application.auth.dto import *
from src.application.user.mapper import UserMapper
from src.application.auth.exceptions import ApplicationException, MismatchedPasswords
from src.infrastructure.db.repositories.user_repository import UserRepository
from src.domain.common.exception import DomainException
from src.config import JwtConfig

jwt_config = JwtConfig()


class JwtService:
    def generate_token(
            self,
            payload: dict,
            private_key: str = jwt_config.private_key_path.read_text(),
            algorithm: str = jwt_config.algorithm,
            minutes: int = jwt_config.expiration_in_minutes
    ) -> str:
        to_encode_payload = payload.copy()
        current_time = datetime.now()
        expiration = current_time + timedelta(minutes=minutes)
        to_encode_payload.update({'exp': expiration, 'iat': current_time})
        jwt_token = jwt.encode(to_encode_payload, private_key, algorithm)
        return jwt_token

    def decode_jwt(self, token: str, private_key: str, algorithm: str) -> dict:
        return jwt.decode(token, private_key, algorithm)


@dataclass
class AuthorizationService:
    user_query_service: UserQueryService
    user_command_service: UserCommandService
    jwt_service: JwtService
    mapper: UserMapper

    async def register(self, registration_dto: RegistrationRequestDto) -> RegistrationResponseDto:
        try:
            await self.user_query_service.check_user_existance(registration_dto.login)
            await self.user_command_service.save_user(
                self.mapper.convert_registration_dto_to_full_user_dto(registration_dto)
            )
            return RegistrationResponseDto('You have been successfully regirested!')
        except (ApplicationException, DomainException) as error:
            return RegistrationResponseDto(error.message)
        except Exception as error:
            return RegistrationResponseDto(str(error))

    async def authenticate(self, authentication_dto: AuthenticationRequestDto) -> AuthenticationResponseDto:
        try:
            user = await self.user_query_service.get_user(authentication_dto.login)
            self.verify_passwords(authentication_dto.password, user.password)
            return AuthenticationResponseDto(
                token=self.jwt_service.generate_token(payload={
                    'sub': f'{user.name} {user.surname}',
                    'username': user.login,
                    'email': user.login
                }),
                verdict='You have been successfully authenticated'
            )
        except (ApplicationException, DomainException) as error:
            return AuthenticationResponseDto(token='-', verdict=error.message)
        except Exception as error:
            return AuthenticationResponseDto(token='-', verdict=str(error))

    def logout(self, logout_dto: LogoutRequestDto) -> LogoutResponseDto:
        if logout_dto.token is not None:
            return LogoutResponseDto('You have been successfully logout from your account! Please, remove a jwt token '
                                     'from your Authorization Headers) I\'m so lazy to do it)')
        return LogoutResponseDto('You have not been authenticated!')

    def verify_passwords(self, raw_password: str, hashed_password: str) -> None:
        if CryptContext(schemes=["bcrypt"], deprecated="auto") \
                .hash(raw_password, salt="a"*21 + "e") != hashed_password:
            raise MismatchedPasswords()
