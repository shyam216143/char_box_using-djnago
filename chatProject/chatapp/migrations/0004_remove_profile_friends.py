# Generated by Django 4.1 on 2022-09-07 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0003_chat_mes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='friends',
        ),
    ]