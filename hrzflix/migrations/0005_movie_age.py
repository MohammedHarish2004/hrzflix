# Generated by Django 5.0.2 on 2024-02-27 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrzflix', '0004_alter_genre_create_at_alter_theme_create_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='age',
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
    ]
