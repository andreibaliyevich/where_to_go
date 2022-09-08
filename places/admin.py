from django.contrib import admin
from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image


class PlaceAdmin(admin.ModelAdmin):
    """ PlaceModel for admin """
    list_display = ('id', 'title', 'description_short')
    inlines = (ImageInline,)


admin.site.register(Place, PlaceAdmin)
