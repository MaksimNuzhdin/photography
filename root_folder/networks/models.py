from django.db import models

# Create your models here.
class Networks(models.Model):
    nw_name=models.CharField(max_length=200,verbose_name='Social network')
    nw_img=models.ImageField(verbose_name='Social network')
    nw_link=models.CharField(max_length=500, verbose_name='Link')
    def __str__(self) -> str: #делаем записи в бд читаемыми
        return self.nw_name
    class Meta:
        verbose_name='Social network'
        verbose_name_plural='Social network'