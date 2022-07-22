from django.contrib import admin

# Register your models here.
from .models import Profile, Meal

admin.site.register(Profile)
admin.site.register(Meal)
