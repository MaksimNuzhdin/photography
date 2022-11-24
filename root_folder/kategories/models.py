from django.db import models

# Create your models here.
class kategories(models.Model):
    category=models.CharField(max_length=200,verbose_name='categories')
    category_dis=models.TextField(verbose_name='Discription', null=True, default='-')
    def __str__(self) -> str: #делаем записи в бд читаемыми
        return self.category
    class Meta:
        verbose_name='Categories'
        verbose_name_plural='Categories'