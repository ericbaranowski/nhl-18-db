# Generated by Django 2.0 on 2018-03-07 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='defensemen_rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='forwards_rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='team',
            name='goalies_rating',
            field=models.IntegerField(default=0),
        ),
    ]
