from django.db import models
from simple_history.models import HistoricalRecords
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from track.models import Track

from authentication.managers import UserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='Email адрес' ,max_length=255, unique=True)
    first_name = models.CharField(verbose_name='Имя', max_length=255)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255)
    photo = models.ImageField(verbose_name='Фото', upload_to='users/photos', default="")
    bio = models.TextField(verbose_name='О себе', default="")

    is_active = models.BooleanField(verbose_name='Активирован', default=True)
    is_staff = models.BooleanField(verbose_name='Персонал', default=False)
    is_superuser = models.BooleanField(verbose_name='Администратор', default=False)

    history = HistoricalRecords()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta: 
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class UserFavorite(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tracks = models.ManyToManyField(Track, related_name='favorite_tracks')

    def __str__(self):
        return f"{self.user.first_name}'s Favorites"

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'