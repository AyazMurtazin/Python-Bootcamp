import protos.spaceship_pb2_grpc
import protos.spaceship_pb2

import grpc

import argparse

from pydantic import ValidationError

from google.protobuf.json_format import MessageToJson, MessageToDict

from pydant.spaceship_model import Spaceship as PydantSpaceship

import os
from alchemy.models.database import DATABASE_NAME, Session
import alchemy.create_database as db_creator

from alchemy.models.spaceship import Spaceship as BaseSpaceship
from alchemy.models.officer import Officer

from sqlalchemy.exc import IntegrityError


def parse():
    parser = argparse.ArgumentParser(
        prog="Reporting client", description="Get\'s cords returns a spaseships", epilog="programm gets list of floats")
    parser.set_defaults(which='empty')
    subparsers = parser.add_subparsers(help='sub-command help')
    parser_scan = subparsers.add_parser('scan', help='scan help',)
    parser_list_traitors = subparsers.add_parser(
        'list_traitors', help='list_traitors help')
    parser_scan.add_argument('cords', nargs='+', type=float)
    parser_scan.set_defaults(which='scan')
    parser_list_traitors.set_defaults(which='list_traitors')
    return parser.parse_args()


def list_traitors(session: Session):
    session = Session()
    query_ally = session.query(Officer.first_name, Officer.last_name, Officer.rank).\
        join(BaseSpaceship).\
        filter(BaseSpaceship.alignment == 'Ally')

    query_enemy = session.query(Officer.first_name, Officer.last_name, Officer.rank).\
        join(BaseSpaceship).\
        filter(BaseSpaceship.alignment == 'Enemy')

    query_intersection = query_ally.intersect(query_enemy)

    results = query_intersection.all()
    for first_name, last_name, rank in results:
        print(
            f"{{'first_name': '{first_name}', 'last_name': '{last_name}', 'rank': '{rank}'}}")


def _create_spaseship(spaceship_json: dict):
    spaceship = BaseSpaceship(
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


if __name__ == "__main__":
    args = parse()
    db_is_created = os.path.exists(DATABASE_NAME)
    session = Session()
    if not db_is_created:
        db_creator.create_database(False)
    if args.which == 'scan':
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = protos.spaceship_pb2_grpc.FederationScannersAndDetectorsStub(
                channel=channel)
            responses = stub.get_spacehips_in_area(
                protos.spaceship_pb2.Coordinates(cord=args.cords))
            for response in responses:
                try:
                    spaceship = PydantSpaceship(
                        **(MessageToDict(response, preserving_proto_field_name=True)))
                    print(MessageToJson(response, preserving_proto_field_name=True))
                except ValidationError as e:
                    continue
                try:
                    spaceship = _create_spaseship(MessageToDict(
                        response, preserving_proto_field_name=True))
                    session.add(spaceship)
                    session.commit()
                except IntegrityError as e:
                    session.rollback()
    elif args.which == 'list_traitors':
        list_traitors(session)
