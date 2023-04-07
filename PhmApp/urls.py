from django.urls import path,re_path
from Phmapp import views

urlpatterns = [
    path(r'factory',views.factoryApi),
    re_path(r'factory/?(\d+)?',views.factoryApi),
    path(r'sensor', views.sensorApi),
    re_path(r'sensor/?(\d+)?', views.sensorApi)
]
