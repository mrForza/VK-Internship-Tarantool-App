import asyncio
import uvicorn
from fastapi import FastAPI

from config import APIConfig, DbConfig
from src.presentation.api.controllers.user import user_router
from src.presentation.api.controllers.authorization import authorization_router
from src.infrastructure.db.main import init_connection


async def main():
    api_config = APIConfig()
    app = FastAPI(debug=api_config.debug, title='VK Internship Authorization Service', version='1.0.0')
    app.include_router(user_router)
    app.include_router(authorization_router)
    server = uvicorn.Server(
        config=uvicorn.Config(
            app,
            host=api_config.host,
            port=api_config.port,
        )
    )
    await server.serve()


if __name__ == '__main__':
    asyncio.run(init_connection(DbConfig()))
    # print('Hello!')
