from django.urls import path
from . import views

urlpatterns = [
    path('sensor-data/', views.get_sensor_data, name='sensor-data'),
    path('toggle-device/<int:device_id>/', views.toggle_device, name='toggle-device'),
]
