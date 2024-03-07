from alchemy.models.database import create_db, Session
from alchemy.models.spaceship import Spaceship
from alchemy.models.officer import Officer
import alchemy.test as t
from sqlalchemy.exc import IntegrityError

def create_database(load_fake_data: bool = False):
    create_db()
    if load_fake_data:
        _load_test_data(Session())


def _load_test_data(session: Session):
    spaceship = _create_spaseship(t.NORM_JSON_DATA)
    session.add(spaceship)
    session.commit()
    print("NORM PASSED")

    try:
        spaceship = _create_spaseship(t.DUPLICAT_JSON_DATA)
        session.add(spaceship)
        session.commit()
    except IntegrityError as e:
        session.rollback()
        print("DUPLICATE PASSED")

    try:
        spaceship = _create_spaseship(t.DUPLICAT_JSON_DATA_WITH_DIFFER1)
        session.add(spaceship)
        session.commit()
    except IntegrityError as e:
        session.rollback()
        print("DUPLICATE 1 PASSED")

    try:
        spaceship = _create_spaseship(t.DUPLICAT_JSON_DATA_WITH_DIFFER2)
        session.add(spaceship)
        session.commit()
    except IntegrityError as e:
        session.rollback()  
        print("DUPLICATE 2 PASSED")

    spaceship = _create_spaseship(t.JSON_DATA_WITH_IMPOSTOR)
    session.add(spaceship)
    session.commit()
    print("IMPOSTER INPUT PASSED")

    session.close()


def _create_spaseship(spaceship_json: dict):
    spaceship = Spaceship(
        name=spaceship_json['name'],
        alignment=spaceship_json['alignment'],
        spaceship_class=spaceship_json['class'],
        length=spaceship_json['length'],
        crew_size=spaceship_json['crew_size'],
        armed=spaceship_json['armed'],
        officers=[Officer(**officer_data)
                  for officer_data in spaceship_json['officers']]
    )
    return spaceship
