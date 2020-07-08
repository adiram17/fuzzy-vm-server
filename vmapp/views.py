from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import psutil
import socket

#Get Status Server 
def getCpuMemoryDisk(request):
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    response_data = {}
    response_data['cpu'] = cpu
    response_data['memory'] = memory
    response_data['disk'] = disk
    return JsonResponse(response_data)

#Get Response Server 
def getMessage(request):
    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)
    response_data = {}
    response_data['hostname'] = hostname
    response_data['ipaddress'] = ipaddress
    return JsonResponse(response_data)