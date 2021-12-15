from django.contrib import admin
from django.urls import path, include
from app import views
from .views import *

urlpatterns = [
    path('', views.person_func),
    path('<int:pk>/', views.update),
]

