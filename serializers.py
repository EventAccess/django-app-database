from rest_framework import serializers
from .models import Attendant


# This is a serializer for the nfc_id field
class BinaryFieldSerializer(serializers.Field):
    def to_representation(self, value):
        return value.hex()

    def to_internal_value(self, data):
        return bytes.fromhex(data)


class AttendantSerializer(serializers.HyperlinkedModelSerializer):
    nfc_id = BinaryFieldSerializer()

    class Meta:
        model = Attendant
        fields = "__all__"
