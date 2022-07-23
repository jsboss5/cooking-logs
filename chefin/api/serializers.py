from rest_framework import serializers
from .models import Meal


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id', 'title', 'date', 'description', 'user', 'image']