from rest_framework import serializers
from .models import *

class GetDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=GetData
        fields='__all__'