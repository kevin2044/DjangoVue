from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework import status


from listelement.models import Element, Type
from listelement.serializer import ElementSerializer


# Create your views here.
def manualJson(request):
    data = {
        'id': 123,
        'nombre': 'Pepe',
    }
    
    return JsonResponse(data)