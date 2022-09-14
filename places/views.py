from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Place


def index(request):
    features = []
    for place in Place.objects.all():
        features.append({
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.longitude, place.latitude]
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': f'/places/{ place.id }/'
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
    place = get_object_or_404(Place, pk=pk)

    imgs = []
    for img in place.images.all():
        imgs.append(img.image.url)

    data = {
        'title': place.title,
        'imgs': imgs,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.longitude,
            'lat': place.latitude
        }
    }
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})
