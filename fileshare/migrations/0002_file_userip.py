# Generated by Django 4.1 on 2022-08-13 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileshare', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='userip',
            field=models.GenericIPAddressField(default=''),
            preserve_default=False,
        ),
    ]
