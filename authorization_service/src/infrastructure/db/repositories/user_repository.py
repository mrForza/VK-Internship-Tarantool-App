from src.infrastructure.db.common.repository import TarantoolRepositoy


class UserRepository(TarantoolRepositoy):
    def get_all_users(self):
        pass

    def get_user_by_id(self, user_id: int):
        pass

    def get_user_by_login(self, login: str):
        pass

    def create_user(self, data: dict):
        pass
