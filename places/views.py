from django.http import JsonResponse
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

    imgs = []
    for img in place.image_set.all():
        imgs.append(img.image.url)

    data = {
        'title': place.title,
        'imgs': imgs,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.coordinates_lng,
            'lat': place.coordinates_lat
        }
    }
    return JsonResponse(data,
        safe=False, json_dumps_params={'ensure_ascii': False})
