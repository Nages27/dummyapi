from django.shortcuts import render
from rest_framework.views import APIView
from dummy.models import User
from dummy.serialized import serializeduser
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status




class to(APIView):
    def post(self,request):
        serial=serializeduser(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data,status=status.HTTP_201_CREATED)
        return  Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)
    


