from sqlalchemy import Column, Integer, String, ForeignKey

from sqlalchemy.orm import relationship

from alchemy.models.database import Base


class Officer(Base):
    __tablename__ = 'officers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    rank = Column(String)
    spaceship_name = Column(String, ForeignKey('spaceships.name'))
    spaceship = relationship('Spaceship', back_populates='officers')
    
    def __repr__(self):
        info: str = f'Spaceship [ID:{self.id}, Alignment: {self.alignment}, Name: {self.name}, Spaceship class: {self.spaceship_class}, Length: {self.length}, Crew size: {self.crew_size}, Armed: {self.armed}]'
        return info