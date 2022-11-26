# Generated by Django 4.1 on 2022-09-28 18:55

import datetime
from django.db import migrations, models
import fileshare.models


class Migration(migrations.Migration):

    dependencies = [
        ('fileshare', '0007_alter_file_datetime_alter_file_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 5, 18, 55, 30, 760603, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to=fileshare.models.content_file_name),
        ),
    ]