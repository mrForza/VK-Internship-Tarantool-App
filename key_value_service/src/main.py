from fastapi import FastAPI

from config import APIConfig
from src.presentation.api.controllers.key_value import key_value_router

app = FastAPI(debug=APIConfig().debug, title='VK Internship Key-Value Service', version='1.0.0')

app.include_router(key_value_router)
