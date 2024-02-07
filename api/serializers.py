from rest_framework import serializers
from .models import Works, Workers


class WorksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Works
        fields = [
            'name_work',
            'max_workers',
            'zarplata'
        ]


class WorkersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Workers
        fields = [
            'first_name',
            'second_name',
            'otchestvo',
            'date_rojdenia',
            'work',
            'stavka',
            'salary'
        ]