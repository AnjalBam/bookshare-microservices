
from django.core.management.base import BaseCommand

from core.helpers.consumers import consumer_map

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
          parser.add_argument('consumer', type=str)

    def handle(self, *args, **options):
            # start_consumers()
            consumer = options.get('consumer', None)
            try: 
                self.stdout.write(self.style.NOTICE(f'Starting consumer `{consumer}`...'))
                consumer_map[consumer]()
            except KeyError as e:
                  self.stdout.write(self.style.ERROR(f'Consumer `{consumer}` not found'))
                  return None