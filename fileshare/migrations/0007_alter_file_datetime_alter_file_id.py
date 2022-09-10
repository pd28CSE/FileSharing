# Generated by Django 4.1 on 2022-09-10 12:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileshare', '0006_alter_file_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 17, 12, 51, 41, 739172, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='file',
            name='id',
            field=models.PositiveBigIntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
