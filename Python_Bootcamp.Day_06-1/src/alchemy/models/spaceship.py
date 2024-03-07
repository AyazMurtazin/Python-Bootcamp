from sqlalchemy import Column, Integer, String, Float, Boolean

from sqlalchemy.orm import relationship

from alchemy.models.database import Base


class Spaceship(Base):
    __tablename__ = 'spaceships'
    alignment = Column(String)
    name = Column(String, primary_key=True)
    spaceship_class = Column(String)
    length = Column(Float)
    crew_size = Column(Integer)
    armed = Column(Boolean)
    officers = relationship('Officer', back_populates='spaceship')

    def __repr__(self):
        info: str = f'Spaceship [Alignment: {self.alignment}, Name: {self.name}, Spaceship class: {self.spaceship_class}, Length: {self.length}, Crew size: {self.crew_size}, Armed: {self.armed}]'
        return info