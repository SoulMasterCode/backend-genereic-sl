# Django
from django.http import Http404

# Models
from django.contrib.auth.models import User
from .models import Profile
from rest_framework.authtoken.models import Token

# User Serializers
from .serializers import *

# Rest Framework 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Authentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# User Views

# User Serializer

class UserSignIn(APIView):
# Crear Nuevo Usuario
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Crea el token
            user = User.objects.get(username=request.data['username'])
            Token.objects.get_or_create(user=user)
            # Fin de la creacion del token
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class UserList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
    
    # Lista usuarios
    def get(self, request, format=None):
        listUser = User.objects.all()
        serializer = UserSerializer(listUser, many=True)
        return Response(serializer.data)
    
class UserDetail(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        token = Token.objects.get(user=user)
        serializer = TokenSerializer(token)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status.HTTP_204_NO_CONTENT)

class ProfileSignIn(APIView):
    # Crear Nuevo Perfil
    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


# Profile Serializer
class ProfileList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
    # Lista usuarios
    def get(self, request, format=None):
        listProfile = Profile.objects.all()
        serializer = ProfileViewSerializer(listProfile, many=True)
        return Response(serializer.data)
    
class ProfileDetail(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = ProfileViewSerializer(profile)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, data= request.data)
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status.HTTP_204_NO_CONTENT)

class LoginView(APIView):
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
