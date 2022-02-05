from django.shortcuts import redirect, render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.http import HttpResponse, JsonResponse
from rest_framework .response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
@api_view(['POST','GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def user_registration(request,pk=None):
    
    if request.method=='POST':
        serializer=User_RegistarionSerializer(data=request.data)
        name=request.data["name"]
        email=request.data["email"]
        contact=request.data["contact"]
        address=request.data["address"]
        
        if serializer.is_valid()==True:
            user_registration=User_Registarion.objects.create(name=name, email=email, contact=contact, address=address)

            if user_registration:
                Login.objects.create(user_id=user_registration.id,contact_1=user_registration.contact)

            return Response ("User Registration Done")


    if request.method=='GET':
        data=[]
        user_detail={}
        user_id=User_Registarion.objects.all().values()
        for detail in user_id:
            user_detail["id"]=detail["id"]
            user_detail["name"]=detail["name"]
            user_detail["email"]=detail["email"]
            user_detail["contact"]=detail["contact"]
            user_detail["address"]=detail["address"]

            if user_detail["contact"] !=" ":
                data.append(user_detail.copy())

            else:
                return Response("User not Registered")

        return Response(data)

    if request.method=='PUT':
        user_id=request.data["user_id"]
        User_Registarion.objects.filter(id=user_id).delete()
        
        serializer=User_RegistarionSerializer(data=request.data)
        name=request.data["name"]
        email=request.data["email"]
        contact=request.data["contact"]
        address=request.data["address"]
        
        if serializer.is_valid()==True:
            user_registration=User_Registarion.objects.create(name=name, email=email, contact=contact, address=address)

            if user_registration:
                Login.objects.create(user_id=user_registration.id,contact_1=user_registration.contact)

            return Response ("User Registration Updated")

    if request.method=='DELETE':
        id = pk
        User_Registarion.objects.get(pk=id).delete()
       
        return Response('Deleted')

class UserLogin(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    def post(self, request):
        login_detail=Login.objects.all()
        contact=request.data["contact_2"]
        
        for cont in login_detail:
            if contact==cont.contact_1:

                return Response ('loggin')

        return Response("User Credintial Not Match")
