from .consumers import *
from .producer import *

def listen_to_consumers():
    print('Listening...')
    listen_to_queue.start()
    