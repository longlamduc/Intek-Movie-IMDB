# Generated by Django 2.1.5 on 2019-03-10 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20190310_0511'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='trailer',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]