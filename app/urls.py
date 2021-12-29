from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', views.person_func),
    path('<int:pk>/', views.update),
    path('clients/', views.PersonViewAPI.as_view()),
    path('clients-detail/<int:pk>/', views.PersonDetailViewAPI.as_view()),
    path('clients-generic-create/', views.GenericAPI.as_view()),
    path('clients-generic-create/<int:id>/', views.GenericAPIpk.as_view()),
    #in generic views pk will get listed in the look_up filed attribute in get and put functions can interpret it differnetly
]

