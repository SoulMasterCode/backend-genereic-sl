"""Generic_sl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Django
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

# Orders Views
# from orders.views import * as order_view

# User Views
from users import views

# Order Views
from orders import views as order_views

urlpatterns = [
    # Users Urls
    path('admin/', admin.site.urls),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('profiles/', views.ProfileList.as_view()),
    path('profiles/<int:pk>', views.ProfileDetail.as_view()),
    path('login/', views.LoginView.as_view()),
    path('user_signin/', views.UserSignIn.as_view()),
    # path('profile_signin/', views.ProfileSignIn.as_view()),
    # Orders Urls
    path('categories/', order_views.CategoryList.as_view()),
    path('categories/<int:pk>', order_views.CategoryDetail.as_view()),
    path('profile_companies/', order_views.ProfileComapanyList.as_view()),
    path('profile_companies/<int:pk>', order_views.ProfileComapanyDetail.as_view()),
    path('products/', order_views.ProductList.as_view()),
    path('products/<int:pk>', order_views.ProductDetail.as_view()),
    path('orders/', order_views.OrderList.as_view()),
    path('orders/<int:pk>', order_views.OrderDetail.as_view()),
    path('product_Has_Orders/', order_views.ProductHasOrderList.as_view()),
    path('product_Has_Orders/<int:pk>', order_views.ProductHasOrderDetail.as_view()),
    # path('profile_company_signin/', order_views.ProfileComapanySignIn.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
