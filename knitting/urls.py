from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('patterns/', views.patterns, name='patterns'),
    path('tutorials/', views.tutorials, name='tutorials'),
]
