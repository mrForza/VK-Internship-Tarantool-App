from asynctnt import Connection
from fastapi import FastAPI

from config import APIConfig, DbConfig
from src.presentation.api.controllers.user import user_router
from src.presentation.api.controllers.authorization import authorization_router


app = FastAPI(debug=APIConfig().debug, title='VK Internship Authorization Service', version='1.0.0')

app.include_router(user_router)
app.include_router(authorization_router)
