from django.contrib.gis.db import models

class Shop(models.Model):
    name = models.CharField(max_length=100)
    geom = models.PointField(null=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
