from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('create/', views.personAPI.as_view()),
    path('list/', views.persongetAPI.as_view()),
    path('update/<int:pk>', views.personupdateAPI.as_view()),
    path('retrieve/<int:pk>', views.personretieveAPI.as_view()),
    path('update-retrieve-destroy/<int:pk>',
         views.personupdateretievedestroyAPI.as_view()),
    path('list-create/', views.createlistAPI.as_view()),
    path('class/<int:pk>', views.Personclassapi.as_view()),
    path('filter/', views.Personfilterapi.as_view()),
]
