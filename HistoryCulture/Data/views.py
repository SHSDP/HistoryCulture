from .models import  ArhitectureObject
from .serializers import ListObjectSerializers,ObjectSerializers
from rest_framework import generics

class ObjectList(generics.ListCreateAPIView):
    queryset = ArhitectureObject.objects.all()
    serializer_class = ListObjectSerializers

class Object(generics.RetrieveAPIView):
    queryset =  ArhitectureObject.objects.all()
    serializer_class = ObjectSerializers
    lookup_field = 'id' 