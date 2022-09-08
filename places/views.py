from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
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


def place_detail(request, pk):
    """ Place detail """
    place = get_object_or_404(Place, pk=pk)
    return HttpResponse(place.title)
