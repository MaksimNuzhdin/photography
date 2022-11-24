from django.contrib import admin
from .models import About
from django.utils.safestring import mark_safe

# Register your models here.
class AboutAdm(admin.ModelAdmin):
    list_display=('ab_title','get_image')
    list_display_links=('ab_title', )
    fields= ('ab_title','get_image', 'ab_photo', 'ab_text')
    readonly_fields=('get_image',)
    def get_image(self, obj):
        if obj.ab_photo:
            return mark_safe(f'<img src="{obj.ab_photo.url}", width="80px">')
        else: return 'No image'
    get_image.short_description='Mini image'

admin.site.register(About, AboutAdm)
