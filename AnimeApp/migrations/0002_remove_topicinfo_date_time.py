# Generated by Django 3.2.8 on 2021-10-12 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AnimeApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topicinfo',
            name='Date_time',
        ),
    ]
