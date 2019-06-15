from django.db import models
from django.contrib.postgres.fields import JSONField

# Model Profile and user
# from users.models import Profile
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):

    """Category es la clase categoria de las empresas, que define el tipo de empresas, ejemplo: manufacturera, comercial ect."""
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=450)

    def __str__(self):
        return self.name

class Profile_company(models.Model):
    """Clase perfil de compania"""

    #user es la llave que relaciona con la clase user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #category es la llave que relaciona Profile_company con category
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    company_name = models.CharField(max_length=100, blank=True)
    telephone = models.CharField(max_length=10, blank=True)
    picture = models.ImageField(upload_to ='company/pictures', null= True, blank= True)
    location = models.DecimalField(max_digits=19, decimal_places=10, blank=True, null=True)
    rfc = models.CharField(max_length=15, blank=True, null=True)
    addres = models.CharField(max_length=250, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.user

class Product(models.Model):
    """Clase productos"""
    #Llave foranea que relaciona con la clase perfil de compania
    profile_company = models.ForeignKey(Profile_company, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=45)
    #precio
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = JSONField()
    #La proviedad status es para dar de baja un producto
    status = models.BooleanField()
    picture = models.ImageField(upload_to ='product/pictures', null= True, blank= True)

    def __str__(self):
        return self.product_name

class Order(models.Model):
    """Clase de ordenes"""
    #Llave foranea que relaciona el perfil de usuario comprador
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    #estado de la orden, cancelada o exitosa
    status = models.BooleanField()
    #Posicion en latitud y longitud
    location = models.DecimalField(max_digits=30, decimal_places=2)
    total_price = models.DecimalField(max_digits=11, decimal_places=2)
    user_ranking = models.SmallIntegerField()
    company_ranking = models.SmallIntegerField()

    def __str__(self):
        return str(self.pk)


class Product_Has_Order(models.Model):
    """Tabla que relaciona Productos y Ordenes"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    #Cantidad
    amount = models.SmallIntegerField()

    def __str__(self):
        return self.product.product_name





