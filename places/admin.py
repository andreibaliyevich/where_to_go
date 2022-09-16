from adminsortable2.admin import SortableAdminBase, SortableTabularInline
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Place, Image


class ImageInline(SortableTabularInline):
    model = Image
    fields = ('image', 'get_preview', 'position')
    readonly_fields = ('get_preview',)

    def get_preview(self, obj):
        if obj.image.height < 200:
            img_height = obj.image.height
        else:
            img_height = 200

        return mark_safe('<img src="{url}" height="{height}" />'.format(
            url=obj.image.url,
            height=img_height,
        ))
    get_preview.short_description = 'Предварительный просмотр'


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title', 'description_short')
    inlines = (ImageInline,)
