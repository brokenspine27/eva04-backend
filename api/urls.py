from django.urls import path
from . import views

urlpatterns = [
    path('personas/', views.get_personas),
    ]