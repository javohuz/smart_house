from django.http import JsonResponse
from .models import Device

def get_sensor_data(request):
    data = {
        "temperature": "25°C",
        "light": "Bright"
    }
    return JsonResponse(data)

def toggle_device(request, device_id):
    device = Device.objects.get(id=device_id)
    device.status = not device.status
    device.save()
    return JsonResponse({"status": device.status})
