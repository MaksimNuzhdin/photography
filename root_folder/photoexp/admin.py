from django.contrib import admin
from.models import PhotoExp
from django.utils.safestring import mark_safe
class PhotoAdm(admin.ModelAdmin):
    list_display=('id','name_img', 'category_ph','get_image')
    list_display_links=('id', 'name_img')
    list_editable=('category_ph',)
    fields=('name_img','category_ph','get_image','photo_img')
    list_filter=('category_ph',)
    readonly_fields=('get_image',)
    list_per_page=10
    list_max_show_all=100
    def get_image(self, obj):
        if obj.photo_img:
            return mark_safe(f'<img src="{obj.photo_img.url}", width="80px">')
        else: return 'No image'
    get_image.short_description='Mini image'
# Register your models here.
admin.site.register(PhotoExp,PhotoAdm)
