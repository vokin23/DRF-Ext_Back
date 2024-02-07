from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import WorksSerializers, WorkersSerializers
from .models import Works, Workers


class BaseWorkWorkersViewSet(viewsets.ModelViewSet):
    @action(detail=True)
    def get_data(self, request):
        data = self.get_object().values()  # Получение данных, предположительно из модели или другого источника
        print(data)
        return Response(data)  # Возвращаем данные в формате JSON


class WorksViewSet(BaseWorkWorkersViewSet):
    queryset = Works.objects.all()
    serializer_class = WorksSerializers


class WorkerViewSet(BaseWorkWorkersViewSet):
    queryset = Workers.objects.all()
    serializer_class = WorkersSerializers
