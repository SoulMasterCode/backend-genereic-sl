from django.contrib import admin

#models
from .models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

