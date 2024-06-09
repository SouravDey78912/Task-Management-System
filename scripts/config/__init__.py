from pydantic import Field
from pydantic_settings import BaseSettings


class _Services(BaseSettings):
    PORT: int = Field(default=6869, validation_alias="service_port")
    HOST: str = Field(default="0.0.0.0", validation_alias="service_host")
    SECURE_ACCESS: bool = Field(default=True)


class _Redis(BaseSettings):
    REDIS_URI: str = Field()


class _Mongo(BaseSettings):
    MONGO_URI: str = Field()


Services = _Services()
Redis = _Redis()
Mongo = _Mongo()

__all__ = ["Services", "Redis", "Mongo"]
