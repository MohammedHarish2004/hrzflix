# Generated by Django 5.0.2 on 2024-02-27 08:31

import django.db.models.deletion
import hrzflix.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('movie_image', models.ImageField(upload_to=hrzflix.models.getfilename)),
                ('description', models.CharField(max_length=100)),
                ('rating', models.FloatField()),
                ('duration', models.CharField(max_length=20)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hrzflix.genre')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hrzflix.theme')),
            ],
        ),
    ]
