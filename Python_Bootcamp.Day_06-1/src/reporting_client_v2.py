import protos.spaceship_pb2_grpc
import protos.spaceship_pb2
import grpc
import argparse
from pydantic import ValidationError
from google.protobuf.json_format import MessageToJson, MessageToDict

from pydant.spaceship_model import Spaceship


def parse():
    parser = argparse.ArgumentParser(
        prog="Reporting client", description="Get\'s cords returns a spaseships", epilog="programm gets list of floats")
    parser.add_argument('cords', nargs='+', type=float)
    return parser.parse_args().cords


if __name__ == "__main__":
    coordinates = parse()
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = protos.spaceship_pb2_grpc.FederationScannersAndDetectorsStub(
            channel=channel)
        responses = stub.get_spacehips_in_area(
            protos.spaceship_pb2.Coordinates(cord=coordinates))
        for response in responses:
            try:
                spaceship = Spaceship(
                    **(MessageToDict(response, preserving_proto_field_name=True)))
                print(MessageToJson(response, preserving_proto_field_name=True))
            except ValidationError as e:
                print(e)
