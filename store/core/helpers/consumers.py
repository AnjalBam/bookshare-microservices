import telnetlib, pika, time
from decouple import config

MQ_HOST = config("RABBIT_MQ_HOST", default="localhost")

import threading
stop_event = threading.Event()

AUTH_EVENTS = 'auth_events'

def get_mq_connection():
    try:
        tel = telnetlib.Telnet(MQ_HOST, "5672", 10)
        tel.close()
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=MQ_HOST),
        )
        if not connection:
            print('no connection')
            return get_mq_connection()
        return connection
    except ConnectionRefusedError as e:
        print("error", e)
        print("Rabbit MQ not open. Trying again in 3s")
        time.sleep(3)
        get_mq_connection()

def listen_to_queue():
    connection = get_mq_connection()
    try:
        channel = connection.channel()
    except Exception as e:
        print(e)
        print('QUEUE:: retrying...')
        listen_to_queue()
    channel.queue_declare(queue="hello")

    def callback(ch, method, properties, body):
        print("QUEUE:: [x] Received %r" % body)

    channel.basic_consume(queue="hello", on_message_callback=callback, auto_ack=True)

    print("QUEUE:: [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()
    connection.close()


def listen_to_auth_events():
    AUTH_QUEUE_NAME = 'auth0'
    connection = get_mq_connection()
    try:
        channel = connection.channel()
    except Exception as e:
        print(e)
        print('AUTH:: retrying...')
        listen_to_auth_events()
    channel.queue_declare(queue=AUTH_QUEUE_NAME)
    channel.exchange_declare(exchange=AUTH_EVENTS, exchange_type="fanout")

    channel.queue_bind(exchange=AUTH_EVENTS, queue=AUTH_QUEUE_NAME)

    def callback(ch, method, properties, body):
        print("AUTH:: [x] Received %r" % body)

    channel.basic_consume(queue=AUTH_QUEUE_NAME, on_message_callback=callback, auto_ack=True)

    print(" AUTH:: [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()
    connection.close()


def listen_to_queue_2():
    connection = get_mq_connection()
    try:
        channel = connection.channel()
    except Exception as e:
        print(e)
        print('QUEUE2:: retrying...')
        listen_to_queue_2()
    channel.queue_declare(queue="test")

    def callback(ch, method, properties, body):
        print("QUEUE2:: [x] Received %r" % body)

    channel.exchange_declare(exchange=AUTH_EVENTS, exchange_type="fanout")
    channel.exchange_declare(exchange='test_exchange', exchange_type="fanout")

    channel.queue_bind(exchange=AUTH_EVENTS, queue="test")
    channel.queue_bind(exchange="test_exchange", queue="test")

    channel.basic_consume(queue="test", on_message_callback=callback, auto_ack=True)

    print(" QUEUE2:: [*] Waiting for messages. To exit press CTRL+C here")
    channel.start_consuming()
    connection.close()



consumer_map = {
    'auth': listen_to_auth_events,
    'queue_2': listen_to_queue_2,
    'queue': listen_to_queue
}


def start_consumers(): 
    print('Starting consumers [[NOT IN USE ANYMORE]]')