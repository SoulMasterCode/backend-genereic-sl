# Django
from django.contrib.auth import authenticate

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

# Los serielizers con View en su nombre son para visualizar y los que no son Serializers para los protocolos Post y Put   

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # Se usara el modelo User
        model = User
        fields=('pk','username','password', 'email','first_name','last_name')

    # Sobrescribiendo el metodo create
    def create(self, validated_data):
        # Orders Models
        from orders.models import Profile_company

        # Creando los perfiles
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user)
        Profile_company.objects.create(user=user)
        return user

    # Sobrescribiendo el metodo update para validar los datos
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
    # Serializador anidado de user al mostrar un serializador anidado me permite ver el contenido de este siempre y cuando haya una relasion 
    user = UserSerializer(many = False, read_only=True)
    class Meta:
        model = Token
        fields = ('key', 'user')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('pk', 'user', 'telephone', 'created', 'modified', 'is_active')

    def create(self, validated_data):
        return Profile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.Profile.user)
        instance.telephone = validated_data.get('telephone', instance.Profile.telephone)
        instance.picture = validated_data.get('picture', instance.Profile.picture)
        instance.save()
        return instance

class ProfileViewSerializer(serializers.ModelSerializer):
    # Serializador anidado de usuario al mostrar un serializador anidado me permite ver el contenido de este siempre y cuando haya una relasion 
    user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Profile
        fields = ('pk', 'user', 'is_active' ,'telephone', 'created', 'modified', 'user')

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
        # Tomando los parametros del request
        username = data.get("username")
        password = data.get("password")
        profile_type = data.get("profile_type")
        
        # Inicializando la variable
        login_user = None
        # user = authenticate(username=username, password=password)

        # Validando si no esta nulo el username y el password
        if not username or not password:
            raise serializers.ValidationError("El campo usuario/contraseña es requerido animal")
        else:
            # Se consulta el usuario
            user = User.objects.filter(username=username)
        # Validando si el usuario existe
        if user.exists():
            # si existe toma el usuario
            login_user = user.first()
        else:
            raise serializers.ValidationError("No existe el usuario xc")
        # si existe el usuario realiza las validaciones de la contraseña
        if login_user:
            # chacando si la contraseña este correcta
            if not login_user.check_password(password):
                raise serializers.ValidationError("Contraseña/Usuario Incorrecta papu")
            # Dependiendo de que el profile_type es false o true en el json traera los perfiles correspondientes
            if profile_type:
                customer_profile = Profile.objects.get(user=login_user)
                data["customer_profile"] = customer_profile
            else:
                company_profile = Profile_company.objects.get(user=login_user)
                data["company_profile"] = company_profile


        # Formateo del json
        token = Token.objects.get_or_create(user=login_user)
        data["key"] = token[0]
        
        del data["username"]
        del data["password"]
        
        return data

