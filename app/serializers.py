from .models import *
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Person, Client

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"
        
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
        validators=[UniqueValidator(queryset=Client.objects.all())]
            
                
            
        
        
        
    

        
        
    