import validators
from pydantic import BaseModel
from pydantic.functional_validators import field_validator
from typing import List, Literal
from uuid import UUID


class URL(BaseModel):
    url: str

    @field_validator('url')
    @classmethod
    def validate_x(cls, v: str) -> str:
        if not validators.url(v):
            raise ValueError('Not URL')
        else:
            return v


class URLs(BaseModel):
    urls: List[URL]


class Task(BaseModel):
    id: UUID
    status: Literal["running", "ready"] = "running"
    result: list = []
