# Generated by Django 4.1 on 2022-08-22 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_auth', '0003_alter_userdetails_profile_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetails',
            old_name='profile_pic',
            new_name='profile_image',
        ),
    ]
