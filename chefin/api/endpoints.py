from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('test/', TemplateView.as_view(template_name='api/testing.html')),
]