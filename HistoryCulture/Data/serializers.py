from rest_framework import fields, serializers
from .models import ArhitectureObject,ArhitectureImage,Sources


class ImageSerializers(serializers.ModelSerializer):
    class Meta:
        model  = ArhitectureImage
        fields = '__all__'
        
        
class SourcesSerializers(serializers.ModelSerializer):
    class Meta:
        model  = Sources
        fields = '__all__'
        
        
class ListObjectSerializers(serializers.ModelSerializer):
    class Meta:
        model  =  ArhitectureObject
        fields = ["name","cor_x","cor_y","district","town","image"]
        
        
class ObjectSerializers(serializers.ModelSerializer):
    images = ImageSerializers(many=True, read_only=True)
    sources = SourcesSerializers(many=True, read_only=True)
    class Meta:
        model  = ArhitectureObject
        fields = ["name",'information','images','sources']