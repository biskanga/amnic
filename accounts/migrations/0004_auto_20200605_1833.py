# Generated by Django 3.0.6 on 2020-06-06 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200321_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='images/user-avatar.JPG', upload_to='images/%Y'),
        ),
    ]
