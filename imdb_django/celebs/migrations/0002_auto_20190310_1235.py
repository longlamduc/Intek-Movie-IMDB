# Generated by Django 2.1.5 on 2019-03-10 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celebs', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='celeb',
            unique_together={('first_name', 'last_name')},
        ),
    ]
