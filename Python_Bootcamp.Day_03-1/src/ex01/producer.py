import json
import redis
import time
import random
import logging

logging.basicConfig(level=logging.INFO)

ids = [1111111111,
       2222222222,
       3333333333,
       4444444444,
       5555555555,
       6666666666,
       7777777777,
       8888888888,
       9999999999,
       312312124,
       112111111111
       ]

redis_host = "localhost"
redis_port = 6379
redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

pubsub_channel = "money_transfers"  # Replace with the desired channel name
while True:
    data = {
        "metadata": {
            "from": random.choice(ids),
            "to": random.choice(ids)
        },
        "amount": random.randint(-5000, 5000)
    }
    logging.info(data)
    json_payload = json.dumps(data)
    redis_client.publish(pubsub_channel, json_payload)
    time.sleep(1)
# Optionally, close the Redis connection when done
# redis_client.close()
