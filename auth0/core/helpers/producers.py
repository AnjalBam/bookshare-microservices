from .consumers import get_mq_connection
import pickle


def send_message_to_queue(queue="hello", exchange="", body="Hello World!"):
    connection = get_mq_connection()
    channel = connection.channel()
    # channel.queue_declare(queue="auth0")
    channel.exchange_declare(exchange="auth_events", exchange_type="fanout")
    channel.basic_publish(exchange='auth_events', routing_key="", body=body)
    print(f" [x] Sent '{body}'")
    connection.close()


def broadcast_message(exchange_name=None, message=""):
    if not exchange_name:
        print("No exchange name provided")
        return None
    connection = get_mq_connection()
    channel = connection.channel()

    bin_message = pickle.dumps(message) # convert to binary format for sending over to the queue

    channel.exchange_declare(exchange=exchange_name, exchange_type="fanout")

    channel.basic_publish(exchange=exchange_name, routing_key="", body=bin_message)

    connection.close()
