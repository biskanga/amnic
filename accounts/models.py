from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    state = models.CharField(max_length = 30)
    gender = models.CharField(max_length = 30)
    phone_number = models.CharField(max_length = 20)
    address = models.TextField(max_length = 264)
    registration_date = models.DateTimeField(auto_now_add = True)
    profile_picture = models.ImageField(upload_to = 'images/%Y', default = 'images/user-avatar.JPG')

    def __str__(self):
        return self.user.username