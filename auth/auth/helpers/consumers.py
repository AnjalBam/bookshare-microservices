from django.conf import settings

channel = settings.MQ_CLIENT

def listen_to_queue():
    channel.queue_declare(queue="hello")

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue="hello", on_message_callback=callback, auto_ack=True)

    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


import threading

listen_to_queue = threading.Thread(target=listen_to_queue)
