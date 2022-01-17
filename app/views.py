from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import pagination
from .models import Client, Person
import json
from .mypaginations import *
from rest_framework.views import APIView  # CLASS BASED VIEWS
from rest_framework import viewsets  # ModelViewSets
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes  # CLASS BASED VIEWS
from rest_framework.response import Response
from rest_framework import status
from django.http import *
from rest_framework.parsers import JSONParser
from .serializers import PersonSerializer, ClientSerializer
from rest_framework.mixins import *
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
# listcreate api view and retrieveupdatedestroy apiview can alone both perform all CRUD functions
from django_filters.rest_framework import DjangoFilterBackend
# ENABLE EASY FILTERING PER VIEW
from rest_framework.pagination import PageNumberPagination
# enable pagination i.e. number of records to be displayed per page
from rest_framework.filters import SearchFilter
from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from rest_framework.permissions import IsAuthenticated

#from project.app import serializers


# ----------------------------------------GenericAPIView MIXINS-------------------------------------------
#----------------------------------------------------------------------------------------------------------#

class personAPI(GenericAPIView, CreateModelMixin):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class persongetAPI(GenericAPIView, ListModelMixin):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class personupdateAPI(GenericAPIView, UpdateModelMixin):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class personretieveAPI(GenericAPIView, RetrieveModelMixin):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

# update, retrieve and destroy can be together as they have pk as a parameter in url


class personupdateretievedestroyAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# create and list can be together as they do not have pk parameter in url


class createlistAPI(GenericAPIView, CreateModelMixin, ListModelMixin):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# ---------------------------------------------CLASS BASED VIEWS----------------------------------------


class Personclassapi(APIView):

    def get(self, request, pk, format=None):
        per = Person.objects.all()
        serializer = PersonSerializer(per, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        stu = Person.objects.get(id=pk)
        serializer = PersonSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ---------------------------------FILTERING DJANGO BACKENDS-----------------
# ADD DJANGO FILTER IN SETTINGS
# ADD LIBRARY IN views.py


class Personfilterapi(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    # filter_backends = [DjangoFilterBackend]  # not-mandatory
    filter_fields = ['name']


'''this is django rest-api'''


def main():
    pass


def test1():
    pass


def test22():
    pass


def test3():
    pass


def test4():
    pass


def test5():
    pass


def test6():
    pass
