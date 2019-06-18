# Rest Framework
from rest_framework import serializers

#Models
from .models import *
from django.contrib.auth.models import User

#DataBase Model
from django.db import models

#User serializer
from users import serializers as users_serializer

# Los serielizers con View en su nombre son para visualizar y los que no son Serializers para los protocolos Post y Put    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('pk', 'name', 'description')
    
    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

class ProfileCompnaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile_company       
        fields = ('pk', 'user', 'category',"company_name","telephone","location","rfc","addres","is_active")
    
    def create(self, validated_data):
        return Profile_company.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.category = validated_data.get('category', instance.category)
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.telephone = validated_data.get('telephone', instance.telephone)
        instance.picture = validated_data.get('picture', instance.picture)
        instance.location = validated_data.get('location', instance.location)
        instance.rfc = validated_data.get('rfc', instance.rfc)
        instance.addres = validated_data.get('addres',instance.addres)
        instance.is_active = validated_data.get('is_active',instance.is_active)
        instance.save()
        return instance

class ProfileCompnayViewSerializer(serializers.ModelSerializer):
    # Serializador anidado de user y category al mostrar un serializador anidado me permite ver el contenido de este siempre y cuando haya una relasion 
    user = users_serializer.UserSerializer(many= False, read_only=True)
    category = CategorySerializer(many=False, read_only=True)
    class Meta:
        model = Profile_company       
        fields = ('pk', 'user', 'category',"company_name","telephone","location","rfc","addres","is_active")

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product       
        fields = ('pk', 'profile_company', 'product_name',"price","description","status","picture")
    
    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.profile_company = validated_data.get('profile_company', instance.profile_company)
        instance.product_name = validated_data.get('product_name', instance.product_name)
        instance.price = validated_data.get('price', instance.price)
        instance.picture = validated_data.get('picture', instance.picture)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status',instance.status)
        instance.save()
        return instance

class ProductViewSerializer(serializers.ModelSerializer):
    # Serializador anidado de ProfileCompnay al mostrar un serializador anidado me permite ver el contenido de este siempre y cuando haya una relasion 
    profile_company = ProfileCompnayViewSerializer(many= False, read_only=True)
    class Meta:
        model = Product       
        fields = ('pk', 'profile_company', 'product_name',"price","description","status","picture")

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order       
        fields = ('pk', 'profile', 'location',"total_price","status","user_ranking","company_ranking")
    
    def create(self, validated_data):
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.profile = validated_data.get('profile', instance.profile)
        instance.location = validated_data.get('location', instance.location)
        instance.total_price = validated_data.get('total_price', instance.total_price)
        instance.user_ranking = validated_data.get('user_ranking', instance.user_ranking)
        instance.company_ranking = validated_data.get('company_ranking', instance.company_ranking)
        instance.status = validated_data.get('status',instance.status)
        instance.save()
        return instance

class OrderViewSerializer(serializers.ModelSerializer):
     # Serializador anidado de Profile al mostrar un serializador anidado me permite ver el contenido de este siempre y cuando haya una relasion 
    profile= users_serializer.ProfileViewSerializer(many = False, read_only=True)
    class Meta:
        model = Order       
        fields = ('pk', 'profile', 'location',"total_price","status","user_ranking","company_ranking")


class ProductHasOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Has_Order       
        fields = ('pk', 'product', 'order',"amount")
    
    def create(self, validated_data):
        return Product_Has_Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.product = validated_data.get('product', instance.product)
        instance.order = validated_data.get('order', instance.order)
        instance.amount = validated_data.get('amount',instance.amount)
        instance.save()
        return instance

class ProductHasOrderViewSerializer(serializers.ModelSerializer):
     # Serializador anidado de Product y Order al mostrar un serializador anidado me permite ver el contenido de este siempre y cuando haya una relasion 
    product = ProductViewSerializer(many = False, read_only=False)
    order = OrderViewSerializer(many=False, read_only=True)
    class Meta:
        model = Product_Has_Order       
        fields = ('pk', 'product', 'order',"amount")