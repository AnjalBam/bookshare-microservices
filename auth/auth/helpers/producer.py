from django.conf import settings
import pika


def publish_message(queue_name='', message='', property=''):
    try:
        channel = settings.MQ_CLIENT
        print("declaring queue", channel, settings.MQ_CONNECTION)
        channel.queue_declare(queue="hello")
        # message = input('Type some message: ');
        message = "Hello world"
        print(message)
        channel.basic_publish(exchange="", routing_key="hello", body=message)
        print(f" [x] Sent '{message}'")
    except Exception as err:
        print('error', err)
        # settings.update_channel(settings.MQ_CONNECTION)
        # publish_message(queue_name, body, property)
