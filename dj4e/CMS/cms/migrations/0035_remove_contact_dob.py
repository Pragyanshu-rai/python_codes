# Generated by Django 3.1.6 on 2021-04-15 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0034_auto_20210410_2032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='dob',
        ),
    ]
