# Generated by Django 3.0.8 on 2020-07-08 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vector',
            name='balanca',
            field=models.IntegerField(default=0),
        ),
    ]
