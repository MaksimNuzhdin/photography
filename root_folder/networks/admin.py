from django.contrib import admin
from .models import Networks
from django.utils.safestring import mark_safe
# Register your models here.
class NetworkADM(admin.ModelAdmin):
    list_display=('id','nw_name','nw_link','get_image',)
    list_display_links=('id','nw_name',)
    fields=('nw_name','nw_link','get_image','nw_img')
    readonly_fields=('get_image',)
    def get_image(self, obj):
        if obj.nw_img:
            return mark_safe(f'<img src="{obj.nw_img.url}", width="80px">')
        else: return 'No image'
    get_image.short_description='Mini image'
admin.site.register(Networks, NetworkADM)