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
    path('Users/', views.UserList.as_view()),
    path('Users/<int:pk>', views.UserDetail.as_view()),
    path('Profiles/', views.ProfileList.as_view()),
    path('Profiles/<int:pk>', views.ProfileDetail.as_view()),
    path('login/', views.LoginView.as_view()),
    path('user_signin/', views.UserSignIn.as_view()),
    path('profile_signin/', views.ProfileSignIn.as_view()),
    # Orders Urls
    path('Categories/', order_views.CategoryList.as_view()),
    path('Categories/<int:pk>', order_views.CategoryDetail.as_view()),
    path('Profile_companies/', order_views.ProfileComapanyList.as_view()),
    path('Profile_companies/<int:pk>', order_views.ProfileComapanyDetail.as_view()),
    path('Products/', order_views.ProductList.as_view()),
    path('Products/<int:pk>', order_views.ProductDetail.as_view()),
    path('Orders/', order_views.OrderList.as_view()),
    path('Orders/<int:pk>', order_views.OrderDetail.as_view()),
    path('Product_Has_Orders/', order_views.ProductHasOrderList.as_view()),
    path('Product_Has_Orders/<int:pk>', order_views.ProductHasOrderDetail.as_view()),
    path('profile_company_signin/', order_views.ProfileComapanySignIn.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
