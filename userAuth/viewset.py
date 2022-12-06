from rest_framework import viewsets
from .serializers import *
from .models import *

class GetDataViewset(viewsets.ModelViewSet):
    queryset=GetData.objects.all()
    serializer_class=GetDataSerializer