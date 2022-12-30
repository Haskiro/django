from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Artist(models.Model):
    nickname = models.CharField(verbose_name='Nickname', max_length=255)
    first_name = models.CharField(verbose_name='Имя', max_length=255)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255)
    bio = models.TextField(verbose_name='О себе')
    birth_date = models.DateField(verbose_name='Дата рождения')
    photo = models.ImageField(verbose_name='Фото', upload_to='atrists')

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'
