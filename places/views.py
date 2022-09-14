from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Place
from .utilities import get_feature_dict


def index(request):
    features = [get_feature_dict(place) for place in Place.objects.all()]
    context = {
        'places': {
          "type": "FeatureCollection",
          "features": features,
        },
    }
    return render(request, 'index.html', context)


def place_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    imgs = [img.image.url for img in place.images.all()]
    raw_place = {
        'title': place.title,
        'imgs': imgs,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.longitude,
            'lat': place.latitude,
        }
    }
    return JsonResponse(raw_place, json_dumps_params={'ensure_ascii': False})
