# Generated by Django 4.1 on 2022-08-22 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_auth', '0002_userdetails_updated_time_userdetails_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pic/'),
        ),
    ]
