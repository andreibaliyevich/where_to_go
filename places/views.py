from django.shortcuts import render
from .models import Place


def index(request):
    """ Home page """
    features = []
    for place in Place.objects.all():
        features.append({
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.coordinates_lng, place.coordinates_lat]
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': '/'
            }
        })
    places_json = {
      "type": "FeatureCollection",
      "features": features
    }
    context = {
        'places': places_json,
    }
    return render(request, 'index.html', context)