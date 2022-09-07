from django.contrib import admin
from .models import Place


class PlaceAdmin(admin.ModelAdmin):
    """ PlaceModel for admin """
    list_display = ('id', 'title', 'description_short')


admin.site.register(Place, PlaceAdmin)
