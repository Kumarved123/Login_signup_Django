# Generated by Django 2.2.11 on 2020-03-26 16:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='time_out',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 27, 22, 13, 24, 986607)),
        ),
    ]
