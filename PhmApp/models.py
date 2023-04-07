from django.db import models

# Create your models here.

class Factories(models.Model):
    FactoryId = models.AutoField(primary_key=True)
    FactoryName = models.CharField(max_length=300)
    SensorId = models.TextField(max_length=300)
    FilePath = models.TextField(max_length=300)
    RawData = models.JSONField()
    SpectralData = models.JSONField()

class Sensors(models.Model):
    SensorId = models.AutoField(primary_key=True)
    SensorType = models.CharField(max_length=300)
    RegisterStatus = models.CharField(max_length=300)
