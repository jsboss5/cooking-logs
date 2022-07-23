from django.shortcuts import render
from django.http import JsonResponse
from .models import Meal
from .serializers import MealSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView



class MealList(APIView):

    def get(self, request, format=None):
        # get all the drinks from the db
        meals = Meal.objects.all()

        # serialize them
        serializer = MealSerializer(meals, many=True)

        # return the json
        return Response(serializer.data)

    def post(self, request):
        serializer = MealSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MealDetail(APIView):

    def _check_if_meal_exists(self, id):

        return Meal.objects.filter(pk=id).exists()


    def get(self, request, id):
        # get all the drinks from the db
        if self._check_if_meal_exists(id):
            meal = Meal.objects.get(pk=id)
            serializer = MealSerializer(meal, many=False)
            return Response(serializer.data)

        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):

        if self._check_if_meal_exists(id):
            meal = Meal.objects.get(pk=id)
            serializer = MealSerializer(meal, data=request.data)
            if serializer.is_valid(): 
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        if self._check_if_meal_exists(id):
            meal = Meal.objects.get(pk=id)
            meal.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_404_NOT_FOUND)
