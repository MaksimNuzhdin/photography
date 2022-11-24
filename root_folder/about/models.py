from django.db import models

# Create your models here.
class About(models.Model):
    ab_photo=models.ImageField(max_length=200, upload_to='about/',verbose_name='photo')
    ab_title=models.CharField(max_length=200,verbose_name='title')
    ab_text=models.TextField(verbose_name='text')
    def __str__(self) -> str: #делаем записи в бд читаемыми
        return self.ab_title
    class Meta:
        verbose_name='About page'
        verbose_name_plural='About page'