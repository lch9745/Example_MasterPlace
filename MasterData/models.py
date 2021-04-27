from django.db import models

# Create your models here.




class Country_Data(models.Model):
    name = models.CharField(max_length=30)
    Data_id = models.CharField(max_length=30)
    

class City_Data(models.Model):
    name = models.CharField(max_length=30)
    Data_id = models.CharField(max_length=30)

class Place_Data(models.Model):
    name = models.CharField(max_length=30)
    Data_id = models.CharField(max_length=30)