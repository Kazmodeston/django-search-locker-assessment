from rest_framework import serializers

from . models import Locker

class LockerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locker
        field = '__all__'
