# Generated by Django 3.0.6 on 2020-06-22 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('number_of_tracks', models.IntegerField()),
                ('album_art', models.ImageField(upload_to='uploads/media/images/album_arts/%y/%m/%d')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ['-release_date'],
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('known_as', models.CharField(max_length=60)),
                ('image', models.ImageField(upload_to='uploads/media/images/artist_image/%y/%m/%d')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ['-known_as'],
            },
        ),
        migrations.CreateModel(
            name='GenreAndCategorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('track_lenght', models.FloatField(blank=True)),
                ('track_number', models.IntegerField(blank=True, null=True)),
                ('release_date', models.DateField(blank=True)),
                ('image', models.ImageField(upload_to='uploads/media/images/song_image/%y/%m/%d')),
                ('file', models.FileField(upload_to='uploads/media/files/song_files/%y/%m/%d')),
                ('slug', models.SlugField(default='', unique=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album', to='base.Album')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artist', to='base.Artist')),
                ('featured_artist', models.ManyToManyField(blank=True, to='base.Artist')),
                ('genre', models.ManyToManyField(related_name='genre', to='base.GenreAndCategorie')),
            ],
            options={
                'ordering': ['-release_date'],
            },
        ),
        migrations.AddField(
            model_name='artist',
            name='genre_or_categorie',
            field=models.ManyToManyField(related_name='genre_or_categorie', to='base.GenreAndCategorie'),
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Artist'),
        ),
    ]
