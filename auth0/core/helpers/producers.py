from .consumers import get_mq_connection


def send_message_to_queue(queue="hello", exchange="", body="Hello World!"):
    connection = get_mq_connection()
    channel = connection.channel()
    # channel.queue_declare(queue="auth0")
    channel.exchange_declare(exchange="auth_events", exchange_type="fanout")
    channel.basic_publish(exchange='auth_events', routing_key="", body=body)
    print(f" [x] Sent '{body}'")
    connection.close()
