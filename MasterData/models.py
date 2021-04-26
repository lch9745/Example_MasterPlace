from django.db import models

# Create your models here.

class MasterData(models.Model):
    Country_name = models.CharField(max_length=30)
    City_name = models.CharField(max_length=30)
    Place_name = models.CharField(max_length=30)


    Country_id = models.CharField(max_length=30)
    City_id = models.CharField(max_length=30)
    Place_id = models.CharField(max_length=30)