from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import status
from django.contrib.auth.hashers import make_password #used to hash the password incoming


from .serializers import CustomUserSerializer, StudentSerializer
from .models import CustomUser,Warden,Caretaker,Student,Room

# Create your views here.

class AllRoutes(APIView):
    """
        This view states all the paths that will be available to the user
    """
    def get(self,request):
        routes = [
            "GET / -> Get all route urls",
            "GET /user -> Get info about all users",
            "Get /hostel -> get ingo about all hostels"
        ]

        return Response(routes)
    
#make a api where it contains the data for custom user


class User(APIView):
    
    #to print all the users
    def get(self,request):
        users = CustomUser.objects.all()

        serializer = CustomUserSerializer(users, many = True)

        return Response(serializer.data)
    
    #called when a user wants to signup 
    def post(self,request):
        user_serializer = CustomUserSerializer(data = request.data)

        password = request.data['password']
        password = make_password(password=password) #it is used to hash the incoming password

        if user_serializer.is_valid():
            print(request.data.get("is_student"))
            print(request.data["is_student"])
            if request.data["is_student"] is True:
                child_serializer = StudentSerializer(data = request.data)
                print("child serializer initialised!")
            else:
                return Response("send student response only for now!")

            user = user_serializer.save(password=password)

            if child_serializer.is_valid():
                if request.data.get("is_student") is True:
                    child_serializer.save(student=user)
                else:
                    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(child_serializer.errors,status= status.HTTP_400_BAD_REQUEST)              
                    
            return Response({
                "user": user_serializer.data,
                }, status=status.HTTP_201_CREATED)
        
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # return Response({"message":"Post request for user creation","data":data})
    
