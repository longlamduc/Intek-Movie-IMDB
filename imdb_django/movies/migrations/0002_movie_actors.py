# Generated by Django 2.1.5 on 2019-03-10 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celebs', '0001_initial'),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(blank=True, to='celebs.Celeb'),
        ),
    ]