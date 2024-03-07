from typing import List
from pydantic import BaseModel, field_validator, model_validator, ValidationError, Field

import constants as c
import pydant.tests as t


class Officer(BaseModel):
    first_name: str
    last_name: str
    rank: str


class SpaceshipType(BaseModel):
    length: float
    crew: int
    armed: bool
    enemy: bool


class Corvette(SpaceshipType):
    @field_validator("length")
    def validate_length(cls, value):
        if 80 > value or value > 250:
            raise ValueError(
                f"length: {value} out of Corvette class length range.")
        return value

    @field_validator("crew")
    def validate_crew(cls, value):
        if 4 > value or value > 10:
            raise ValueError(
                f"Crew: {value} out of Corvette class crew range.")
        return value

    @field_validator("armed")
    def validate_armed(cls, value):
        return value

    @field_validator("enemy")
    def validate_enemy(cls, value):
        return value


class Friegate(SpaceshipType):
    @field_validator("length")
    def validate_length(cls, value):
        if 300 > value or value > 600:
            raise ValueError(
                f"length: {value} out of Corvette class length range.")
        return value

    @field_validator("crew")
    def validate_crew(cls, value):
        if 10 > value or value > 15:
            raise ValueError(
                f"Crew: {value} out of Corvette class crew range.")
        return value

    @field_validator("armed")
    def validate_armed(cls, value):
        return value

    @field_validator("enemy")
    def validate_enemy(cls, value):
        if value:
            raise ValueError(f"Hostile: Carrier can\'t be Hostile")
        return value


class Cruiser(SpaceshipType):
    @field_validator("length")
    def validate_length(cls, value):
        if 500 > value or value > 1000:
            raise ValueError(
                f"length: {value} out of Corvette class length range.")
        return value

    @field_validator("crew")
    def validate_crew(cls, value):
        if 15 > value or value > 30:
            raise ValueError(
                f"Crew: {value} out of Corvette class crew range.")
        return value

    @field_validator("armed")
    def validate_armed(cls, value):
        return value

    @field_validator("enemy")
    def validate_enemy(cls, value):
        return value


class Destroyer(SpaceshipType):
    @field_validator("length")
    def validate_length(cls, value):
        if 800 > value or value > 2000:
            raise ValueError(
                f"length: {value} out of Corvette class length range.")
        return value

    @field_validator("crew")
    def validate_crew(cls, value):
        if 50 > value or value > 80:
            raise ValueError(
                f"Crew: {value} out of Corvette class crew range.")
        return value

    @field_validator("armed")
    def validate_armed(cls, value):
        return value

    @field_validator("enemy")
    def validate_enemy(cls, value):
        if value:
            raise ValueError(f"Hostile: Carrier can\'t be Hostile")
        return value


class Carrier(SpaceshipType):
    @field_validator("length")
    def validate_length(cls, value):
        if 1000 > value or value > 4000:
            raise ValueError(
                f"length: {value} out of Corvette class length range.")
        return value

    @field_validator("crew")
    def validate_crew(cls, value):
        if 120 > value or value > 250:
            raise ValueError(
                f"Crew: {value} out of Corvette class crew range.")
        return value

    @field_validator("armed")
    def validate_armed(cls, value):
        if value:
            raise ValueError(f"Armed: Carrier can\'t be armed")
        return value

    @field_validator("enemy")
    def validate_enemy(cls, value):
        return value


class Dreadnought(SpaceshipType):
    @field_validator("length")
    def validate_length(cls, value):
        if 5000 > value or value > 20000:
            raise ValueError(
                f"length: {value} out of Corvette class length range.")
        return value

    @field_validator("crew")
    def validate_crew(cls, value):
        if 300 > value or value > 500:
            raise ValueError(
                f"Crew: {value} out of Corvette class crew range.")
        return value

    @field_validator("armed")
    def validate_armed(cls, value):
        return value

    @field_validator("enemy")
    def validate_enemy(cls, value):
        return value


CLASS_MAPPING = {'Corvette': Corvette, 'Friegate': Friegate, 'Cruiser': Cruiser,
                 'Destroyer': Destroyer, 'Carrier': Carrier, 'Dreadnought': Dreadnought}


class Spaceship(BaseModel):
    alignment: str
    name: str
    length: float
    crew_size: int
    armed: bool
    officers: List[Officer]
    class_: str = Field(..., alias="class")

    @model_validator(mode='after')
    def verify_spaceship(self):
        pydantic_class = CLASS_MAPPING.get(self.class_)
        try:
            pydantic_class(**{"length": self.length, "crew": self.crew_size,
                              "armed": self.armed, "enemy": self.alignment == "Enemy"})
        except ValueError as e:
            raise e
        return self


if __name__ == "__main__":
    def test(test_dict):
        try:
            Spaceship(**test_dict)
            state = True
        except ValidationError as e:
            state = False
        return state
    print("\t\t\t---CLEAR TESTS TRUE---")
    for i in t.CLEAR_TEST_TRUE:
        assert test(i) == True
    print("\t\t\t---CLEAR TESTS FALSE---")
    for i in t.CLEAR_TEST_FALSE:
        assert test(i) == False
    print("\t\t\t---ARMED TESTS TRUE---")
    for i in t.ARMED_TEST_TRUE:
        assert test(i) == True
    print("\t\t\t---ARMED TESTS FALSE---")
    for i in t.ARMED_TEST_FALSE:
        assert test(i) == False
    print("\t\t\t---ENEMY TESTS TRUE---")
    for i in t.ENEMY_TEST_TRUE:
        assert test(i) == True
    print("\t\t\t---ENEMY TESTS FALSE---")
    for i in t.ENEMY_TEST_FALSE:
        assert test(i) == False
