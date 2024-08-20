from asynctnt import Connection
from fastapi import Depends

from src.application.auth.services import (AuthorizationService, JwtService,
                                           UserCommandService,
                                           UserQueryService)
from src.application.user.mapper import UserMapper
from src.config import DbConfig
from src.infrastructure.db.repositories.user_repository import UserRepository


async def get_db_connection() -> Connection:
    connection = Connection(host=DbConfig().host, port=DbConfig().port)
    await connection.connect()
    return connection


def get_user_repo(connection: Connection = Depends(get_db_connection)) -> UserRepository:
    return UserRepository(connection)


def get_user_query_service(repo: UserRepository = Depends(get_user_repo)) -> UserQueryService:
    return UserQueryService(repo)


def get_mapper() -> UserMapper:
    return UserMapper()


def get_user_command_service(
        repo: UserRepository = Depends(get_user_repo),
        mapper: UserMapper = Depends(get_mapper)
) -> UserCommandService:
    return UserCommandService(repo, mapper)


def get_jwt_service() -> JwtService:
    return JwtService()


def get_mapper() -> UserMapper:
    return UserMapper()


async def get_authorization_service(
        user_query_service: UserQueryService = Depends(get_user_query_service),
        user_command_service: UserCommandService = Depends(get_user_command_service),
        jwt_service: JwtService = Depends(get_jwt_service),
        mapper: UserMapper = Depends(get_mapper),
) -> AuthorizationService:
    return AuthorizationService(
        user_query_service,
        user_command_service,
        jwt_service,
        mapper
    )
