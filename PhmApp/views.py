from django.shortcuts import render
from django.views.decorators.csrf import  csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Phmapp.models import Factories, Sensors
from Phmapp.serializers import FactorySerializer, SensorSerializer

# Create your views here.
@csrf_exempt
def factoryApi(request,id=0):
    if request.method=='GET':
        factories = Factories.objects.all()
        factories_serializer = FactorySerializer(factories,many=True)
        return JsonResponse(factories_serializer.data,safe=False)

    elif request.method=='POST':
        factories_data = JSONParser().parse(request)
        factories_serializer = FactorySerializer(data=factories_data)
        if factories_serializer.is_valid():
            factories_serializer.save()
            return JsonResponse("Factories Data Added Successfully",safe=False)
        return JsonResponse("Factories Data Failed to add", safe=False)

    elif request.method=='PUT':
        factories_data = JSONParser().parse(request)
        factories = Factories.objects.get(FactoryId=factories_data['FactoryId'])
        factories_serializer = FactorySerializer(factories,data=factories_data)
        if factories_serializer.is_valid():
            factories_serializer.save()
            return JsonResponse("Factories Data Updated Successfully",safe=False)
        return JsonResponse("Factories Data Failed to update", safe=False)

    elif request.method=='DELETE':
        factories = Factories.objects.get(FactoryId=id)
        factories.delete()
        return JsonResponse("Factories Data Deleted Successfully", safe=False)

@csrf_exempt
def sensorApi(request,id=0):
    if request.method=='GET':
        sensors = Sensors.objects.all()
        sensors_serializer = SensorSerializer(sensors,many=True)
        return JsonResponse(sensors_serializer.data,safe=False)

    elif request.method=='POST':
        sensors_data = JSONParser().parse(request)
        sensors_serializer = SensorSerializer(data=sensors_data)
        if sensors_serializer.is_valid():
            sensors_serializer.save()
            return JsonResponse("Sensors Data Added Successfully",safe=False)
        return JsonResponse("Sensors Data Failed to add", safe=False)

    elif request.method=='PUT':
        sensors_data = JSONParser().parse(request)
        sensors = Sensors.objects.get(SensorId=sensors_data['SensorId'])
        sensors_serializer = SensorSerializer(sensors,data=sensors_data)
        if sensors_serializer.is_valid():
            sensors_serializer.save()
            return JsonResponse("Sensors Data Updated Successfully",safe=False)
        return JsonResponse("Sensors Data Failed to update", safe=False)

    elif request.method=='DELETE':
        sensors = Sensors.objects.get(SensorId=id)
        sensors.delete()
        return JsonResponse("Sensors Data Deleted Successfully", safe=False)