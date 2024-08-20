from fastapi import FastAPI

from config import APIConfig
from src.presentation.api.controllers.authorization import authorization_router

app = FastAPI(debug=APIConfig().debug, title='VK Internship Authorization Service', version='1.0.0')

app.include_router(authorization_router)
