# Generated by Django 5.0.2 on 2024-02-27 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrzflix', '0002_genre_create_at_movie_create_at_movie_trending_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
