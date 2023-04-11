import telnetlib, pika, time

from decouple import config

MQ_HOST = config("RABBIT_MQ_HOST", default="localhost")

STORE_EVENTS = 'store_events'

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
    channel = connection.channel()
    channel.queue_declare(queue="auth0")
    channel.queue_bind(exchange='users', queue="auth0")

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue="auth0", on_message_callback=callback, auto_ack=True)

    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()
    connection.close()


def listen_to_queue_2():
    connection = get_mq_connection()
    try:
        channel = connection.channel()
    except Exception as e:
        print(e)
        print('[TEST] retrying...')
        listen_to_store_events()
    channel.queue_declare(queue="queue_2")

    def callback(ch, method, properties, body):
        print("[TEST] Received %r" % body)

    channel.exchange_declare(exchange=STORE_EVENTS, exchange_type="fanout")
    channel.queue_bind(exchange=STORE_EVENTS, queue="queue_2")

    channel.basic_consume(queue="queue_2", on_message_callback=callback, auto_ack=True)

    print("[TEST] Waiting for messages. To exit press CTRL+C here")
    channel.start_consuming()
    connection.close()

def listen_to_store_events():
    connection = get_mq_connection()
    try:
        channel = connection.channel()
    except Exception as e:
        print(e)
        print('[STORE] retrying...')
        listen_to_store_events()
    channel.queue_declare(queue="store")

    def callback(ch, method, properties, body):
        print("[STORE] Received %r" % body)
    
    channel.exchange_declare(exchange=STORE_EVENTS, exchange_type="fanout")
    channel.queue_bind(exchange=STORE_EVENTS, queue="store")

    channel.basic_consume(queue="store", on_message_callback=callback, auto_ack=True)

    print("[STORE] Waiting for messages. To exit press CTRL+C here")
    channel.start_consuming()
    connection.close()

consumer_map = {
    "test": listen_to_queue_2,
    "store": listen_to_store_events
}


def start_consumers(): 
    print('Starting consumers [[NOT USED ANYMORE]]')
    # listen_to_queue.start()
    # listen_to_queue.join()
    # listen_to_queue_2.start()
    # listen_to_queue_2.join()