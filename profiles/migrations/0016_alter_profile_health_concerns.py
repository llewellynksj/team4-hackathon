# Generated by Django 3.2.23 on 2023-11-24 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0015_alter_profile_health_concerns'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='health_concerns',
            field=models.ManyToManyField(blank=True, to='profiles.Tag'),
        ),
    ]