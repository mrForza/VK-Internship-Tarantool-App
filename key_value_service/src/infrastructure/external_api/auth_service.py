import requests

from src.application.exceptions import UserIsNotAuthorized


class ExternalApiService:
    def check_authorization(self, headers: dict) -> None:
        print('#' * 10, headers.get('authorization'))
        response = requests.post(
            url='http://authorization_service:8080/auth/check/',
            json={'authorization': headers.get('authorization', '')}
        )
        if 'NO' in response.text:
            raise UserIsNotAuthorized()
