from django.shortcuts import render
from rest_framework import viewsets

from .serializers import WorksSerializers, WorkersSerializers
from .models import Works, Workers


class WorksViewSet(viewsets.ModelViewSet):
    queryset = Works.objects.all()
    serializer_class = WorksSerializers


class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Workers.objects.all()
    serializer_class = WorkersSerializers
