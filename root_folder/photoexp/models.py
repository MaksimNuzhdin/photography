from django.db import models
from kategories.models import kategories
from django.views.generic import DetailView
from django.shortcuts import render

# Create your models here.
class PhotoExp(models.Model):
    photo_img=models.ImageField(max_length=200, upload_to='examples/',verbose_name='eximg')
    name_img=models.CharField(max_length=200, verbose_name='Name')
    category_ph=models.ForeignKey(kategories,on_delete=models.PROTECT, null=True, blank=True, verbose_name='Category')
    def __str__(self) -> str: #делаем записи в бд читаемыми
        return self.name_img
    class Meta:
        verbose_name='My gallery'
        verbose_name_plural='My gallery'
class PhototDetail(DetailView):
    model=kategories
    
    
    template_name='./album_page.html'
    context_object_name='category'
    def album_page(request):
        kategories_list=kategories.objects.all()
        photo_list=PhotoExp.objects.get(category_ph=kategories_list.get(category_ph=kategories.category))
        
        
        dict_obj={'photo_list':photo_list}
        return render(request, './album_page.html', dict_obj)


