from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from punchinout.api.v1.serializer import timeinserializer,timeoutserializer
from punchinout.models import timein,timeout,User

import requests
from django.shortcuts import render


def get_context(status, success, message, data):
    """
    This helps us to reading the json easil,
    for help of this function we can easily figure out what our falut or where the code is broke
    the out put of this fuction is ---->>
                status = status.HTTP_200_OK,
                success=False,
                message=f"This is trial",
                data={}
    
    1. get_context(status, success, message, data):
        a. status is return HTTP respone
        b. success is booloen feild , it return the method is suceess or not
        c. message is string , it return the massage what we wrote
        d. data is return api
    """
    context = {}
    
    context["status"] = status
    context["success"] = success
    context["message"] = message
    context["data"] = data
    
    return Response(context, status = status)

class timeinview(APIView):
    def post(self,request):
        serializer = timeinserializer(data=request.data)
        if serializer.is_valid():
            try:
                
                serializer.save()
                context = get_context(
                        status=status.HTTP_200_OK,
                        success=True,
                        message=f'Punch In  Succesfully',
                        data = serializer.data
                    )
                return context
            except:
                context = get_context(
                        status=status.HTTP_406_NOT_ACCEPTABLE,
                        success=True,
                        message=f'Data is not acceptable',
                        data = serializer.errors
                    )
                return context
        else:
            context = get_context(
                        status=status.HTTP_400_BAD_REQUEST,
                        success=True,
                        message=f'serializer is not valid',
                        data = serializer.errors
                    )
            return Response(serializer.errors)

    def get(self,request,pk=None):
        if pk is not None:
            try:
                times = timein.objects.get(pk=pk)
                serializer = timeinserializer(times)
                context = get_context(
                        status=status.HTTP_200_OK,
                        success=True,
                        message=f'Time in of user {times.userid} ({times.firstname})',
                        data = serializer.data
                    )
                return Response(data=serializer.data)
            except:
                context = get_context(
                        status=status.HTTP_200_OK,
                        success=True,
                        message=f'no data found of given userid {pk}',
                        data = 'none'
                    )
                return Response(data=serializer.errors)
        else:
            try:
                times = timein.objects.all()
                serializer = timeinserializer(times,many=True)
                context = get_context(
                    status=status.HTTP_200_OK,
                    success=True,
                    message=f'Users time are',
                    data = serializer.data
                )
                return Response(data=serializer.data)
            except:
                return Response("Error happens")
        
class timeoutview(APIView):
    def post(self,request):
        serializer = timeoutserializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                context = get_context(
                        status=status.HTTP_200_OK,
                        success=True,
                        message=f'Punch out Succesfully',
                        data = serializer.data
                    )
                return context
            except:
                context = get_context(
                        status=status.HTTP_406_NOT_ACCEPTABLE,
                        success=True,
                        message=f'Data is not acceptable',
                        data = serializer.errors
                    )
                return context
        else:
            context = get_context(
                        status=status.HTTP_400_BAD_REQUEST,
                        success=True,
                        message=f'serializer is not valid',
                        data = serializer.errors
                    )
            return Response(serializer.errors)

    def get(self,request,pk=None):
        if pk is not None:
            try:
                times = timeout.objects.get(pk=pk)
                serializer = timeoutserializer(times)
                context = get_context(
                        status=status.HTTP_200_OK,
                        success=True,
                        message=f'Time in of user {times.userid} ({times.firstname})',
                        data = serializer.data
                    )
                return context
            except:
                context = get_context(
                        status=status.HTTP_200_OK,
                        success=True,
                        message=f'no data found of given userid {pk}',
                        data = 'none'
                    )
                return context
        else:
            try:
                times = timeout.objects.all()
                serializer = timeoutserializer(times,many=True)
                context = get_context(
                    status=status.HTTP_200_OK,
                    success=True,
                    message=f'Users time are',
                    data = serializer.data
                )
                return context
            except:
                return Response("Error happens")

def PunchInPage(request):
    response = requests.get('http://127.0.0.1:8000/punchinout/timein/')
    data = response.json()
    return render(request,'punchin.html',{'data':data})