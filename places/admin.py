from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    fields = ('image', 'get_preview', 'position')
    readonly_fields = ('get_preview',)

    def get_preview(self, obj):
        if obj.image.height < 200:
            img_height = obj.image.height
        else:
            img_height = 200

        return mark_safe('<img src="{url}" height={height} />'.format(
            url=obj.image.url,
            height=img_height,
        )
    )


class PlaceAdmin(admin.ModelAdmin):
    """ PlaceModel for admin """
    list_display = ('id', 'title', 'description_short')
    inlines = (ImageInline,)


admin.site.register(Place, PlaceAdmin)
