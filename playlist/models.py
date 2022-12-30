from tabnanny import verbose
from django.db import models
from track.models import Track

# Create your models here.
class Playlist(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание')
    tracks = models.ManyToManyField(verbose_name='Треки', to=Track, related_name='playlists')
    cover = models.ImageField(verbose_name='Обложка', upload_to='playlists/covers')

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = 'Плейлист'
        verbose_name_plural = 'Плейлисты'