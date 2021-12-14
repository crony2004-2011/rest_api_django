from django.shortcuts import render
from .models import Person
from django.http import *
from rest_framework.parsers import *
from .serializers import PersonSerializer
# Create your view

def person_func(request):
    if request.method == 'GET':
        person = Person.objects.all()
        serializer = PersonSerializer(person, many=True)
        return JsonResponse(serializer.data, safe = False)
    elif request.method == 'POST':
        data = JSONParser().parser(request.data)
        serializer = PersonSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    
        
    
        
    