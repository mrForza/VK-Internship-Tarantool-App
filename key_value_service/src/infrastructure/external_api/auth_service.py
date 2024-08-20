import requests

from src.application.exceptions import UserIsNotAuthorized
from src.config import EXTERNAL_API_HOST


class ExternalApiService:
    def check_authorization(self, headers: dict) -> None:
        response = requests.post(
            url=f'{EXTERNAL_API_HOST}/api/check/',
            json={'authorization': headers.get('authorization', '')}
        )
        if 'NO' in response.text:
            raise UserIsNotAuthorized()
