from pydoc import describe
from tabnanny import verbose
from django.db import models
from artist.models import Artist

# Create your models here.
class Track(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    artist = models.ManyToManyField( verbose_name='Исполнители', to=Artist, related_name='tracks')
    audio_file = models.FileField(verbose_name='Файл', upload_to='tracks/audio')
    cover = models.ImageField(verbose_name='Обложка', upload_to='tracks/covers')
    released_at = models.DateField(verbose_name='Дата выпуска', auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = 'Трек'
        verbose_name_plural = 'Треки'