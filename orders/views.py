# Django
from django.shortcuts import render
from  django.http import Http404

#Models
from .models import *
from django.contrib.auth.models import User
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

# Orders Views

class CategoryList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    # Lista de categorias
    def get(self, request, format=None):
        categoryList = Category.objects.all()
        serializer = CategorySerializer(categoryList, many=True)
        return Response(serializer.data)

    # Crear Nuevo Usuario
    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
class CategoryDetail(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response(status.HTTP_204_NO_CONTENT)

class ProfileComapanySignIn(APIView):
     # Crear Nuevo Perfil de empresa
    def post(self, request, format=None):
        serializer = ProfileCompnaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class ProfileComapanyList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    # Lista de categorias
    def get(self, request, format=None):
        profileComapanyList = Profile_company.objects.all()
        serializer = ProfileCompnayViewSerializer(profileComapanyList, many=True)
        return Response(serializer.data)
    
class ProfileComapanyDetail(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    def get_object(self, pk):
        try:
            return Profile_company.objects.get(pk=pk)
        except Profile_company.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        profile_category = self.get_object(pk)
        serializer = ProfileCompnayViewSerializer(profile_category)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        profile_category = self.get_object(pk)
        serializer = ProfileCompnaySerializer(profile_category, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        profile_category = self.get_object(pk)
        profile_category.delete()
        return Response(status.HTTP_204_NO_CONTENT)

class ProductList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    # Lista de categorias
    def get(self, request, format=None):
        productList = Product.objects.all()
        serializer = ProductViewSerializer(productList, many=True)
        return Response(serializer.data)

    # Crear Nuevo Usuario
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
class ProductDetail(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductViewSerializer(product)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status.HTTP_204_NO_CONTENT)

class OrderList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    # Lista de categorias
    def get(self, request, format=None):
        orderList = Order.objects.all()
        serializer = OrderViewSerializer(orderList, many=True)
        return Response(serializer.data)

    # Crear Nuevo Usuario
    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
class OrderDetail(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        order = self.get_object(pk)
        serializer = OrderViewSerializer(order)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        order = self.get_object(pk)
        serializer = OrderSerializer(order, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        order = self.get_object(pk)
        order.delete()
        return Response(status.HTTP_204_NO_CONTENT)

class ProductHasOrderList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    # Lista de categorias
    def get(self, request, format=None):
        productHasOrderList = Product_Has_Order.objects.all()
        serializer = ProductHasOrderViewSerializer(productHasOrderList, many=True)
        return Response(serializer.data)

    # Crear Nuevo Usuario
    def post(self, request, format=None):
        serializer = ProductHasOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
class ProductHasOrderDetail(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    def get_object(self, pk):
        try:
            return Product_Has_Order.objects.get(pk=pk)
        except Product_Has_Order.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        product_has_order = self.get_object(pk)
        serializer = ProductHasOrderViewSerializer(product_has_order)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        product_has_order = self.get_object(pk)
        serializer = ProductHasOrderSerializer(product_has_order, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        product_has_order = self.get_object(pk)
        product_has_order.delete()
        return Response(status.HTTP_204_NO_CONTENT)