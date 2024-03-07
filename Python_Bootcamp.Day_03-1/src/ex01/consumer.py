import redis
import argparse
import json
import logging

logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser(description='manager of redis queue')
parser.add_argument('-e', '--bad-guys', required=True, help='Comma separated 10char identifiers')
args = parser.parse_args()
bad_guys = [int(i) for i in args.bad_guys.split(',') if i.isdigit()]

redis_host = "localhost"
redis_port = 6379
redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

pubsub_channel = "money_transfers"
pubsub = redis_client.pubsub()
pubsub.subscribe(pubsub_channel)

for message in pubsub.listen():
    try:
        if message['type'] == 'message':
            message_data = json.loads(message["data"])
            message_metadata = message_data["metadata"]
            msg_from = message_metadata["from"]
            msg_to = message_metadata["to"]
            if 10 ** 10 > msg_to > 10 ** 9 and 10 ** 10 > msg_from > 10 ** 9:
                if message_data["amount"] > 0 and msg_to in bad_guys:
                    message_metadata["to"], message_metadata["from"] = message_metadata["from"], message_metadata["to"]
                    logging.info('---swapped---')
                print(f"{message_data}")
                logging.info(message_data)
    except:
        pass

# Close the Redis connection (if needed)
# redis_client.close()
