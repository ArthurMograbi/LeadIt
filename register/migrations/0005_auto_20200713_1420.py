# Generated by Django 3.0.8 on 2020-07-13 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_auto_20200711_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='vgen',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='client',
            name='age',
            field=models.CharField(default=18, max_length=3),
        ),
        migrations.AlterField(
            model_name='client',
            name='cel',
            field=models.CharField(default='NC', max_length=20),
        ),
        migrations.AlterField(
            model_name='client',
            name='cpf',
            field=models.CharField(default='NC', max_length=20),
        ),
    ]
