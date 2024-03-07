from concurrent import futures
import grpc
import protos.spaceship_pb2
import protos.spaceship_pb2_grpc
import random
import constants as c

SPACESHIPS = [[0, [80, 250], [4, 10]], [1, [300, 600], [10, 15]], [2, [500, 1000], [15, 30]], [
    3, [800, 2000], [50, 80]], [4, [1000, 4000], [120, 250]], [5, [5000, 20000], [300, 500]]]


class Server(protos.spaceship_pb2_grpc.FederationScannersAndDetectorsServicer):
    def get_spacehips_in_area(self, request, context):
        print(f'Сoordinates: {request.cord}')
        # super().get_spacehips_in_area(request, context)
        return self.generate_spaceships()

    # def generate_spaceships(self):
    #     for _ in range(random.randint(1, 1000)):
    #         alignment = random.randint(0, 1)
    #         spaceship = protos.spaceship_pb2.Spaceship(**{
    #             "alignment": alignment,
    #             "name": random.choice(c.SPASESHIP_NAMES),
    #             "length": random.randint(1, 20000),
    #             "class": random.randint(0, 5),
    #             "crew_size": random.randint(0, 500),
    #             "armed": bool(random.randint(0, 1)),
    #             "officers": [{"first_name": random.choice(c.FIRST_NAMES),
    #                 "last_name": random.choice(c.LAST_NAMES),
    #                 "rank": random.choice(c.RANKS)}for _ in range(0 if alignment == 'Enemy' else 1, 10)]
    #         })

    #         yield spaceship
    def generate_spaceships(self):
        for _ in range(random.randint(1, 100)):
            alignment = random.randint(0, 1)
            spshp = random.choice(SPACESHIPS)
            spaceship = protos.spaceship_pb2.Spaceship(**{
                "alignment": alignment,
                "name": random.choice(c.SPASESHIP_NAMES),
                "length": random.randint(*(spshp[1])),
                "class": spshp[0],
                "crew_size": random.randint(*(spshp[2])),
                "armed": bool(random.randint(0, 1)),
                "officers": [{"first_name": random.choice(c.FIRST_NAMES),
                              "last_name": random.choice(c.LAST_NAMES),
                              "rank": random.choice(c.RANKS)}for _ in range(0 if alignment == 'Enemy' else 1, 10)]
            })

            yield spaceship


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    protos.spaceship_pb2_grpc.add_FederationScannersAndDetectorsServicer_to_server(
        Server(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
