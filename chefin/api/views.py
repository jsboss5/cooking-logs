from django.shortcuts import render
from django.http import JsonResponse
from .models import Meal
from .serializers import MealSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def meal_list(request):


    if request.method == "GET":
        # get all the drinks from the db
        meals = Meal.objects.all()

        # serialize them
        serializer = MealSerializer(meals, many=True)

        # return the json
        return Response(serializer.data)

    if request.method == "POST":
        serializer = MealSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def meal_detail(request, id):

    try:
        meal = Meal.objects.get(pk=id)

    except Meal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        # get all the drinks from the db
        serializer = MealSerializer(meal, many=False)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = MealSerializer(meal, data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        meal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
