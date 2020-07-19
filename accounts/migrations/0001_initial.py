# Generated by Django 3.0.2 on 2020-03-20 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=264)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('profile_picture', models.ImageField(default='images/user_avatar.png', upload_to='images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
