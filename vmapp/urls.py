from django.urls import path
from . import views

urlpatterns = [
    path("getCpuMemoryDisk/", views.getCpuMemoryDisk, name="getCpuMemoryDisk"),
    path("getMessage/", views.getMessage, name="getMessage"),
]
