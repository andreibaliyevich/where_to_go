import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Place, Image


class Command(BaseCommand):
    help = 'Loading Place'

    def add_arguments(self, parser):
        parser.add_argument(
            '--url',
            dest='url',
            required=True,
            help='the url to process',
        )

    def handle(self, *args, **options):
        r = requests.get(options['url'])
        data = r.json()

        place, is_create = Place.objects.get_or_create(
            title=data['title'],
            description_short=data['description_short'],
            description_long=data['description_long'],
            longitude=data['coordinates']['lng'],
            latitude=data['coordinates']['lat'],
        )

        if is_create:
            k = 1
            for img_url in data['imgs']:
                name = img_url.split('/')[-1]
                img_r = requests.get(img_url)
                file = ContentFile(img_r.content, name)
                Image.objects.create(place=place, image=file, position=k)
                k += 1
