# Generated by Django 3.2.23 on 2023-11-23 12:39

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_rename_user_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(default='media/placeholder.svg', max_length=255, verbose_name='image'),
        ),
    ]
