from django.http import JsonResponse
from .models import Sensors
from .serializers import SensorsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def sensors_list(request, format=None):

    if request.method == 'GET':
        sensors = Sensors.objects.all()
        serializer = SensorsSerializer(sensors, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = SensorsSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
@api_view(['GET', 'PUT', 'DELETE'])
def sensors_detail(request, id, format=None):
    
    try:
        sensor = Sensors.objects.get(pk=id)
    except Sensors.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    if request.method == 'GET':
        serializer = SensorsSerializer(sensor)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = SensorsSerializer(sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
            
    elif request.method == 'DELETE':
        sensor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)