from pydantic import BaseModel, Field, PositiveInt
from typing import Literal, List, Generator


class PossibleAnswer(BaseModel):
    answer: str
    result: bool


class Question(BaseModel):
    question: str
    answers: List[PossibleAnswer]


class Questions(BaseModel):
    questions: List[Question]


class Indications(BaseModel):
    respiration: PositiveInt = Field(ge=0, le=100)
    heart_rate: PositiveInt = Field(ge=0, le=300)
    blushing_level: Literal[1, 2, 3, 4, 5, 6]
    pupillary_dilation: PositiveInt = Field(ge=0, le=10)


class NormalIndications(BaseModel):
    respiration: PositiveInt = Field(ge=12, le=16)
    heart_rate: PositiveInt = Field(ge=60, le=100)
    blushing_level: Literal[1, 2, 3, 4, 5, 6] = Field(le=3)
    pupillary_dilation: PositiveInt = Field(ge=2, le=8)


class Answer(BaseModel):
    answer: PossibleAnswer
    indications: Indications


class Answers(BaseModel):
    answers: List[Answer]
