from django.db import models
from track.models import Track
from artist.models import Artist

# Create your models here.
class Album(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание')
    tracks = models.ManyToManyField(verbose_name='Треки', to=Track, related_name='albums')
    cover = models.ImageField(verbose_name='Обложка', upload_to='albums/covers')
    artist = models.ManyToManyField(verbose_name='Исполнители', to=Artist, related_name='albums')

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'