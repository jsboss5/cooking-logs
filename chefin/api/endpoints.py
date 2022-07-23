from django.urls import path
from . import views as MealViews
from django.views.generic import TemplateView


urlpatterns = [
    path('test/', TemplateView.as_view(template_name='api/testing.html')),
    path('meals/', MealViews.meal_list),
    path('meals/<int:id>', MealViews.meal_detail)
]