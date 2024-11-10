from rest_framework import serializers
from .models import Attendant


class AttendantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attendant
        fields = '__all__'
