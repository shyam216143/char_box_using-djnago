# Generated by Django 4.1 on 2022-09-07 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0004_remove_profile_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(related_name='my_friends', to='chatapp.friend'),
        ),
    ]
