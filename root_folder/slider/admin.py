from django.contrib import admin
from .models import Slider
from django.utils.safestring import mark_safe
# Register your models here.
class SliderAdm(admin.ModelAdmin):
    list_display=('id', 'slider_title', 'get_image')
    list_display_links=('id', 'slider_title',)
    fields=('slider_title','get_image','slider_img')
    readonly_fields=('get_image',)
    def get_image(self, obj):
        if obj.slider_img:
            return mark_safe(f'<img src="{obj.slider_img.url}", width="80px">')
        else: return 'Нет картинки'
    get_image.short_description='Миниатюра'
admin.site.register(Slider, SliderAdm)
