from django.db import models

# Model User
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=10)
    picture = models.ImageField(upload_to='profile/pictures', blank=True, null=True)
    is_active = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

# class CustomUser(AbstractUser):
#     telephone = models.CharField(max_length=10)