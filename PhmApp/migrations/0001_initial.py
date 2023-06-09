# Generated by Django 4.1.4 on 2023-04-07 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Factories",
            fields=[
                ("FactoryId", models.AutoField(primary_key=True, serialize=False)),
                ("FactoryName", models.CharField(max_length=300)),
                ("SensorId", models.TextField(max_length=300)),
                ("FilePath", models.TextField(max_length=300)),
                ("RawData", models.JSONField()),
                ("SpectralData", models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name="Sensors",
            fields=[
                ("SensorId", models.AutoField(primary_key=True, serialize=False)),
                ("SensorType", models.CharField(max_length=300)),
                ("RegisterStatus", models.CharField(max_length=300)),
            ],
        ),
    ]
