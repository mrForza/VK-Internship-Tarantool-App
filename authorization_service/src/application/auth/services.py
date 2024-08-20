import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext

from src.application.user.services import UserQueryService, UserCommandService
from src.application.auth.dto import *
from src.application.user.mapper import UserMapper
from src.application.auth.exceptions import UserIsNotAuthorized, IncorrectLoginOrPassword
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

    def validate_jwt_token(self, token: str) -> bool:
        try:
            decoded = jwt.decode(
                token,
                key=jwt_config.public_key_path.read_text(),
                algorithms=[jwt_config.algorithm]
            )
            return True
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return False
        except Exception:
            return False


@dataclass
class AuthorizationService:
    user_query_service: UserQueryService
    user_command_service: UserCommandService
    jwt_service: JwtService
    mapper: UserMapper

    async def register(self, registration_dto: RegistrationRequestDto) -> RegistrationResponseDto:
        await self.user_query_service.check_user_existance(registration_dto.login)
        await self.user_command_service.save_user(
            self.mapper.convert_registration_dto_to_full_user_dto(registration_dto)
        )
        return RegistrationResponseDto('You have been successfully registered!')

    async def authenticate(self, authentication_dto: AuthenticationRequestDto) -> AuthenticationResponseDto:
        user = await self.user_query_service.get_user(authentication_dto.login)
        self.verify_passwords(authentication_dto.password, user.password)
        return AuthenticationResponseDto(
            token=self.jwt_service.generate_token(payload={
                'sub': f'{user.name} {user.surname}',
                'username': user.login,
                'email': user.login
            }),
            message='You have been successfully authenticated'
        )

    def logout(self, logout_dto: LogoutRequestDto) -> LogoutResponseDto:
        if 'YES' in self.check(CheckRequestDto(authorization=logout_dto.token)).authorized:
            return LogoutResponseDto('You have been successfully logout from your account! Please, remove a jwt token '
                                     'from your Authorization Headers) I\'m so lazy to do it)')
        raise UserIsNotAuthorized()

    def check(self, check_dto: CheckRequestDto) -> CheckResponseDto:
        authorization_header = check_dto.authorization
        if authorization_header is None or authorization_header == '':
            return CheckResponseDto('NO')

        data = authorization_header.split(' ')
        if len(data) != 2:
            return CheckResponseDto('NO')
        bearer, token = data
        if bearer is None or token is None:
            return CheckResponseDto('NO')

        if not self.jwt_service.validate_jwt_token(token):
            return CheckResponseDto('NO')
        return CheckResponseDto('YES')

    def verify_passwords(self, raw_password: str, hashed_password: str) -> None:
        if CryptContext(schemes=["bcrypt"], deprecated="auto") \
                .hash(raw_password, salt="a" * 21 + "e") != hashed_password:
            raise IncorrectLoginOrPassword()
