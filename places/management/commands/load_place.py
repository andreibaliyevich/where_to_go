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

        place = Place.objects.get_or_create(
            title=data['title'],
            description_short=data['description_short'],
            description_long=data['description_long'],
            coordinates_lng=data['coordinates']['lng'],
            coordinates_lat=data['coordinates']['lat'],
        )

        k = 1
        for img_url in data['imgs']:
            name = img_url.split('/')[-1]
            img_r = requests.get(img_url)
            content = ContentFile(img_r.content)
            img = Image(place=place[0], position=k)
            img.image.save(name, content, save=False)
            img.save()
            k += 1
