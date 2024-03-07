import protos.spaceship_pb2_grpc
import protos.spaceship_pb2
import grpc
import argparse

from google.protobuf.json_format import MessageToJson


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
        try:
            responses = stub.get_spacehips_in_area(
                protos.spaceship_pb2.Coordinates(cord=coordinates))
            for response in responses:
                print(MessageToJson(response, preserving_proto_field_name=True))
        except grpc.RpcError as e:
            status_code = e.code()
            details = e.details()
            print(
                f"Error in gRPC call. Status code: {status_code}, Details: {details}")
