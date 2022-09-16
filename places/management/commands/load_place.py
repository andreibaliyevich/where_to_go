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
        response = requests.get(options['url'])
        raw_place = response.json()

        place, created = Place.objects.get_or_create(
            title=raw_place['title'],
            longitude=raw_place['coordinates']['lng'],
            latitude=raw_place['coordinates']['lat'],
            defaults={
                'description_short': raw_place['description_short'],
                'description_long': raw_place['description_long'],
            },
        )

        if created:
            for position, img_url in enumerate(raw_place['imgs']):
                name = img_url.split('/')[-1]
                img_r = requests.get(img_url)
                file = ContentFile(img_r.content, name)
                Image.objects.create(place=place, image=file, position=position)
