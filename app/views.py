from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Client, Person, Client
import json
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.http import *
from rest_framework.parsers import JSONParser
from .serializers import PersonSerializer, ClientSerializer
from rest_framework import serializers
# Create your view
@permission_classes((permissions.AllowAny,))
@api_view(['GET','POST'])
#api_view will replace the function based api view, so we will not need to use the function 
#based http request and we dont need to give out jsonresponse
#In api_view, we do not need to parse the data in post/put methods and use request.data
def person_func(request,parser_context=None):
    if request.method == 'GET':
        person = Person.objects.all() #ORM QUERY
        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        #data = JSONParser().parse(request)
        #will work in function based views
        serializer = PersonSerializer(data = request.data)
        #will work in api_view decorator is used, when input data goes directly to serializer
        if serializer.is_valid():
            serializer.save()
            #return JsonResponse(serializer.data, safe = False)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            #One under api_view, we do not need JsonResponse but only Response and http status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #now we want to update and delete articles by their id's
#@csrf_exempt
#not needed in api_view
@api_view(['GET','PUT','DELETE'])
@permission_classes((permissions.AllowAny,))
def update(request,pk):
    person = Person.objects.get(id=pk) #ORM QUERY
    if request.method == "GET":
        serializer = PersonSerializer(person)
        #return JsonResponse(serializer.data)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        person = Person.objects.get(id=pk) #ORM QUERY
        #data = JSONParser().parse(request)
        serializer = PersonSerializer(person, data=request.data)
        #we do not need to parse the input under api_view function
        if serializer.is_valid():
            serializer.save()
            #return JsonResponse(serializer.data)
            return Response(serializer.data)
        #return JsonResponse(serializer.errors,status=400)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#class based views 

class PersonViewAPI(APIView):
    
    def get(self,request):
        client = Client.objects.all()
        serializer = ClientSerializer(client, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ClientSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PersonDetailViewAPI(APIView):
    def get(self,request,pk):
        client = Client.objects.get(id=pk)
        serializer = ClientSerializer(client)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        client = Client.objects.get(id=pk)
        serializer = ClientSerializer(client, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        client = Client.objects.get(id=pk)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
        
    
        
        
        

    
    
    
    
    
        
    
    
        
    
    
        
    
        
    
        
    