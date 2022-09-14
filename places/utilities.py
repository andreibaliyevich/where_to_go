from os.path import splitext
from django.urls import reverse
from django.utils import timezone


def get_image_path(instance, filename):
    filepath = timezone.now().strftime('%Y/%m/%d/%H%M%S%f')
    file_ext = splitext(filename)[1].lower()
    return f'images/{ filepath }{ file_ext }'


def get_feature_dict(place):
    return {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [place.longitude, place.latitude]
        },
        'properties': {
            'title': place.title,
            'placeId': place.id,
            'detailsUrl': reverse('places:place_detail', args=[place.id])
        }
    }
