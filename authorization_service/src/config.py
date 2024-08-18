from dataclasses import dataclass, field
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


@dataclass
class JwtConfig:
    private_key_path: Path = BASE_DIR / 'certificates' / 'private_key.pem'
    public_key_path: Path = BASE_DIR / 'certificates' / 'public_key.pem'
    algorithm: str = 'RS256'
    expiration_in_minutes: int = 30


@dataclass
class APIConfig:
    host: str = '127.0.0.1'
    port: int = 8080
    jwt_config: JwtConfig = field(default_factory=JwtConfig)
    debug: bool = False


@dataclass
class DbConfig:
    host: str = 'authorization_tarantool_db'
    port: int = 3301
    user: str = 'admin'
    password: str = '123'


@dataclass
class Config:
    api_config: APIConfig = field(default_factory=APIConfig)
    db_config: DbConfig = field(default_factory=DbConfig)
