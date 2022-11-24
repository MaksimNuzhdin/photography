from django.db import models

# Create your models here.
class TeleSettings(models.Model):
    tg_token=models.CharField(max_length=200, verbose_name='Token')
    tg_chat=models.CharField(max_length=200, verbose_name='Chat')
    tg_text=models.TextField(verbose_name='Text')
    def __str__(self) -> str: #делаем записи в бд читаемыми
        return self.tg_chat
    class Meta:
        verbose_name='Settings'
        verbose_name_plural='Settings'