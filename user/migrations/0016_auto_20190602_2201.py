# Generated by Django 2.2.1 on 2019-06-02 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_auto_20190602_2139'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BoardComment',
            new_name='MsgBoard',
        ),
    ]