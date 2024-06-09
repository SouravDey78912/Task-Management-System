from typing import Any

from pydantic import BaseModel, Field


class DefaultResponseSchema(BaseModel):
    status: str = Field(default="success")
    message: str = Field(default="success")
    data: Any = Field(default=None)


class DefaultFailureSchema(DefaultResponseSchema):
    status: str = Field(default="failure")
    message: str = Field(default="failure")
    error: str = Field(default=None)
