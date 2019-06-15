from django.db import models

# Model User
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
class Profile(models.Model):
    """Clase profile que hereda de AbstractUser para poder usar el logueo que provee django"""
    #LLave que relaciona User con Profile, para poder utilizar sus propiedades.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=10, blank=True)
    picture = models.ImageField(upload_to='profile/pictures', blank=True, null=True)
    #Para activar o desactivar el perfil de vendedor del usuario
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

# class CustomUser(AbstractUser):
#     telephone = models.CharField(max_length=10)