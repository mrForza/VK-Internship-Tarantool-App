from dataclasses import dataclass, field
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


@dataclass
class APIConfig:
    host: str = '127.0.0.1'
    port: int = 9080
    debug: bool = False


@dataclass
class DbConfig:
    host: str = 'key_value_tarantool_db'
    port: int = 3301
    user: str = 'admin'
    password: str = '123'


@dataclass
class Config:
    api_config: APIConfig = field(default_factory=APIConfig)
    db_config: DbConfig = field(default_factory=DbConfig)
