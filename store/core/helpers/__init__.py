import telnetlib, pika, time

MQ_HOST = "bookshare_mq"

import threading
stop_event = threading.Event()

def get_mq_connection():
    try:
        tel = telnetlib.Telnet(MQ_HOST, "5672", 10)
        tel.close()
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=MQ_HOST),
        )
        return connection
    except ConnectionRefusedError as e:
        print("error", e)
        print("Rabbit MQ not open. Trying again in 3s")
        time.sleep(3)
        get_mq_connection()

def listen_to_queue():
    connection = get_mq_connection()
    channel = connection.channel()
    channel.queue_declare(queue="hello")

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue="hello", on_message_callback=callback, auto_ack=True)

    print(" [*] Waiting for messages. To exit press CTRL+C")
    # channel.start_consuming()
    stop_event.set()
    connection.close()


def listen_to_queue_2():
    connection = get_mq_connection()
    channel = connection.channel()
    channel.queue_declare(queue="hello")

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue="hello", on_message_callback=callback, auto_ack=True)

    print(" [*]2 Waiting for messages. To exit press CTRL+C here")
    # channel.start_consuming()
    stop_event.set()
    connection.close()


# print(threading.current_thread())

listen_to_queue = threading.Thread(target=listen_to_queue)
listen_to_queue_2 = threading.Thread(target=listen_to_queue_2)


def start_consumers(): 
    print('Starting consumers')
    listen_to_queue.start()
    listen_to_queue.join()
    listen_to_queue_2.start()
    listen_to_queue_2.join()