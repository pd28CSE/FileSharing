# Generated by Django 4.1 on 2022-08-13 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fileshare', '0004_rename_userip_useripaddress_ipaddress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='qrcode',
        ),
    ]
