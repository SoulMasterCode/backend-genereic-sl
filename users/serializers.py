# Rest Framework
from rest_framework import serializers

# Models
from .models import Profile
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from orders.models import Profile_company

# Data Base Models
from django.db import models
from rest_framework.response import Response

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=('pk','username', 'email', 'password','first_name','last_name')

    def create(self, validated_data):
        from orders.models import Profile_company

        user = User.objects.create_user(**validated_data)
        profile = Profile.objects.create(user=user)
        profile.save()
        profile_company = Profile_company.objects.create(user=user)
        profile_company.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.email = validated_data.get('email', instance.email)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance




# class RegisterUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('pk', 'username', 'email', 'password', 'first_name', 'last_name')

#     def create(self, validated_data):
#         return User.objects.create_user(**validated_data)

class TokenSerializer(serializers.ModelSerializer):
    user = UserSerializer(many = False, read_only=True)
    class Meta:
        model = Token
        fields = ('key', 'user')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('pk', 'user', 'telephone', 'picture', 'created', 'modified', 'is_active')

    def create(self, validated_data):
        return Profile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.Profile.user)
        instance.telephone = validated_data.get('telephone', instance.Profile.telephone)
        instance.picture = validated_data.get('picture', instance.Profile.picture)
        instance.save()
        return instance

class ProfileViewSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Profile
        fields = ('pk', 'user', 'is_active' ,'telephone', 'picture', 'created', 'modified', 'user')

class LoginSerializer(serializers.ModelSerializer):
    # Serializers
    from orders import serializers as orders_serializers

    # Parametros del login
    password = serializers.CharField(required=False, allow_blank=True)
    username = serializers.CharField(required=False, allow_blank=True)
    profile_type = serializers.BooleanField()
    key = serializers.CharField(required=False, allow_blank=True)

    # Serializadores de los perfiles
    customer_profile = ProfileViewSerializer(many=False, read_only=True)
    company_profile = orders_serializers.ProfileCompnayViewSerializer(many=False, read_only=True)
    # token_fields = TokenSerializer(many=False, read_only=True)
    class Meta:
        # Se usara el modelo Token para ahorarnos algunos parametros
        model = Token
        #Agregando los campos nesesarios para el login serializer
        fields = ('username', 'password', 'key', 'profile_type', 'customer_profile', 'company_profile')
        extra_kwards = {'password':{'write_only':True}}
    
    # sobreescribiendo el metodo validate para hacer las validaciones manualmente
    def validate(self, data):
        username = data.get("username")
        password = data.get("password")
        profile_type = data.get("profile_type")
        login_user = None

        if not username or not password:
            raise serializers.ValidationError("El campo usuario/contraseña es requerido animal")
        else:
            user = User.objects.filter(username=username)
        if user.exists():
            login_user = user.first()
        else:
            raise serializers.ValidationError("No existe el usuario xc")
        if login_user:
            if not login_user.check_password(password):
                raise serializers.ValidationError("Contraseña Incorrecta papu")
            if profile_type:
                customer_profile = Profile.objects.get(user=login_user)
                data["customer_profile"] = customer_profile
            else:
                company_profile = Profile_company.objects.get(user=login_user)
                data["company_profile"] = company_profile


        # Formateo de la respuesta
        token = Token.objects.get_or_create(user=login_user)
        data["key"] = token[0]
        
        del data["username"]
        del data["password"]
        
        return data

