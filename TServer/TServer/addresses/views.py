from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Addresses
from .migrations.serializers import AddressesSeriallizers
from rest_framework.parsers import JSONParser
# Create your views here.

def address_list(request):
    if request.method=='GET':
        query_set=Addresses.objects.All()
        serializer=AddressesSeriallizers(query_set, many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=AddressesSeriallizers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors, status=400)
