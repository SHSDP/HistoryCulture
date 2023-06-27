from django.db import models

    
class ArhitectureObject(models.Model):
    name = models.CharField(max_length=40)
    information = models.CharField(max_length=1000)
    cor_x = models.FloatField()
    cor_y = models.FloatField()
    district = models.CharField(max_length=40)
    town = models.CharField(max_length=40)
    image = models.CharField(max_length=200) 
    
    
    
class ArhitectureImage(models.Model):
    name = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    license = models.CharField(max_length=70)
    url = models.CharField(max_length=200)
    obj = models.ForeignKey(ArhitectureObject, on_delete=models.CASCADE,related_name='images')
   
   
    
class Sources(models.Model):
    text = models.CharField(max_length=100)  
    obj = models.ForeignKey(ArhitectureObject, on_delete=models.CASCADE,related_name='sources')
    