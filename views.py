from rest_framework import viewsets
from database.serializers import AttendantSerializer
from database.models import Attendant


class AttendantViewSet(viewsets.ModelViewSet):
    queryset = Attendant.objects.all()
    serializer_class = AttendantSerializer
