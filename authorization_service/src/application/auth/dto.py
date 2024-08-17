from dataclasses import dataclass


@dataclass(frozen=True)
class RegistrationRequestDto:
    login: str
    password: str
    name: str
    surname: str


@dataclass(frozen=True)
class RegistrationResponseDto:
    verdict: str


@dataclass(frozen=True)
class AuthenticationRequestDto:
    login: str
    password: str


@dataclass(frozen=True)
class AuthenticationResponseDto:
    verdict: str


@dataclass(frozen=True)
class LogoutResponseDto:
    verdict: str
