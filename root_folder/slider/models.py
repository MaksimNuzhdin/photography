from django.db import models

# Create your models here.
class Slider (models.Model):
    slider_img=models.ImageField(max_length=200, upload_to='sliderimg/', verbose_name='img')
    slider_title=models.CharField(max_length=200, verbose_name='Название')
    # slide_css=models.CharField(max_length=200, null=True, default='-', verbose_name='CSS class')
    def __str__(self) -> str: #делаем записи в бд читаемыми
        return self.slider_title
    class Meta:
        verbose_name='Front Image'
        verbose_name_plural='Front Image'
