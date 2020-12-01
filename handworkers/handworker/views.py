from django.shortcuts import render
from rest_framework.decorators import api_view , permission_classes
from rest_framework import status
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

from .models import Category, City, Workers, Home, RateWorkers, Phone, Governorate
from .serializer import GovernorateSerializer, CategorySerializer, CitySerializer, WorkersSerializer, HomeSerializer
# Create your views here.


@api_view(['GET'])
def home(request):
    if request.method == 'GET':
        data_home = Home.objects.get(id=1)
        if len(data_home) > 0:
            data_rest = HomeSerializer(data_home,)
            data = {'message': 'no data', 'data': data_rest}
            return JsonResponse(data, safe=False, status=status.HTTP_200_OK)
        else:
            data = {'message': 'no data', 'data': []}
            return JsonResponse(data, safe=False, status=status.HTTP_404_NOT_FOUND)



