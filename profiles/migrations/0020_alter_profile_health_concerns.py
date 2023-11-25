# Generated by Django 3.2.23 on 2023-11-25 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0019_alter_profile_health_concerns'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='health_concerns',
            field=models.ManyToManyField(blank=True, related_name='issues', to='profiles.Tag'),
        ),
    ]