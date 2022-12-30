# Generated by Django 4.0.5 on 2022-06-20 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('audio_file', models.FileField(upload_to='tracks/audio', verbose_name='Файл')),
                ('cover', models.ImageField(upload_to='tracks/covers', verbose_name='Обложка')),
                ('released_at', models.DateField(verbose_name='Дата выпуска')),
                ('artist', models.ManyToManyField(related_name='tracks', to='artist.artist', verbose_name='Исполнители')),
            ],
            options={
                'verbose_name': 'Трек',
                'verbose_name_plural': 'Треки',
            },
        ),
    ]
