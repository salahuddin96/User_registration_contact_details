from .models import *
from rest_framework import serializers

class User_RegistarionSerializer(serializers.ModelSerializer):
    class Meta:
        model=User_Registarion
        fields = ['id','name','email','contact','address']

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=Login
        fields = ['id','contact_1']