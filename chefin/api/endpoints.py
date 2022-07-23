from django.urls import path
from . import views as MealViews
from .views import MealList, MealDetail
from django.views.generic import TemplateView


urlpatterns = [
    path('test/', TemplateView.as_view(template_name='api/testing.html')),
    path('meals/', MealList.as_view()),
    path('meals/<int:id>', MealDetail.as_view())
]