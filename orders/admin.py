from django.contrib import admin

# class admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# My Models
from .models import *

# Register your models here.
@admin.register(Profile_company)
class ProfileCompanyAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(Product_Has_Order)
class ProductHasOrederAdmin(admin.ModelAdmin):
    pass