# Generated by Django 2.2.1 on 2019-06-02 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_auto_20190602_2201'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MsgBoard',
            new_name='MessageBoard',
        ),
    ]