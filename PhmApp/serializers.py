from rest_framework import serializers
from Phmapp.models import Factories, Sensors

class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Factories
        fields=('FactoryId','FactoryName','SensorId','FilePath','RawData','SpectralData')

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sensors
        fields=('SensorId','SensorType','RegisterStatus')