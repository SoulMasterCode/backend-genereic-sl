# Rest Framework
from rest_framework import serializers

# Models
from .models import Profile
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from orders.models import Profile_company

# Data Base Models
from django.db import models

# Serializers
# from orders import serializers as orders_serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=('pk','username', 'email', 'password','first_name','last_name')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.email = validated_data.get('email', instance.email)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance

# class UserAllSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('pk','username','first_name', 'last_name', 'password', 'email')
    
#     def create(self, validated_data):
#         return User.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.username = validated_data.get('username', instance.username)
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.email = validated_data.get('email', instance.email)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.password = validated_data.get('password', instance.password)
#         instance.save()
#         return instance

class TokenSerializer(serializers.ModelSerializer):
    user = UserSerializer(many = False, read_only=True)
    class Meta:
        model = Token
        fields = ('key', 'user')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('pk', 'user', 'telephone', 'picture', 'created', 'modified')

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
        fields = ('pk', 'user', 'telephone', 'picture', 'created', 'modified', 'user')

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=False, allow_blank=True)
    username = serializers.CharField(required=False, allow_blank=True)
    profile_type = serializers.BooleanField()
    key = serializers.CharField(required=False, allow_blank=True)
    customer_profile = ProfileViewSerializer(many=False, read_only=True)
    # company_profile = orders_serializers.ProfileCompnayViewSerializer(many=False, read_only=True)
    # token_fields = TokenSerializer(many=False, read_only=True)
    class Meta:
        model = Token
        fields = ('username', 'password', 'key', 'profile_type', 'customer_profile', 'company_profile')
        extra_kwards = {'password':{'write_only':True}}
    
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
            else:
                company_profile = Profile_company.objects.get(user=login_user)


        # Formateo de la respuesta
        token = Token.objects.get_or_create(user=login_user)
        data["key"] = token[0]
        data["customer_profile"] = customer_profile
        del data["username"]
        del data["password"]
        
        return data