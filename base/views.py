from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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
    
