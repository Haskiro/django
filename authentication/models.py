from django.db import models
from simple_history.models import HistoricalRecords
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from track.models import Track
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save()
        favs = UserFavorite.objects.create(user=user)
        print(favs)
        favs.save()

        return user

    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(
            email = email,
            first_name = first_name,
            last_name = last_name,
            password = password
        )

        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        
        user.save()

        return user


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
    tracks = models.ManyToManyField(Track, related_name='favorite_tracks', blank=True)

    def __str__(self):
        return f"{self.user.first_name}'s Favorites"

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'