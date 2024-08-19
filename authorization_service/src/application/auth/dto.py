from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class RegistrationRequestDto:
    login: str
    password: str
    name: str
    surname: str
    dict = asdict


@dataclass(frozen=True)
class RegistrationResponseDto:
    message: str
    dict = asdict


@dataclass(frozen=True)
class AuthenticationRequestDto:
    login: str
    password: str
    dict = asdict


@dataclass(frozen=True)
class AuthenticationResponseDto:
    token: str
    message: str
    dict = asdict


@dataclass(frozen=True)
class LogoutRequestDto:
    token: str
    dict = asdict


@dataclass(frozen=True)
class LogoutResponseDto:
    message: str
    dict = asdict


@dataclass(frozen=True)
class CheckRequestDto:
    authorization: str
    dict = asdict


@dataclass(frozen=True)
class CheckResponseDto:
    authorized: str
    dict = asdict
