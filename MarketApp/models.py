from django.db import models


# Create your models here.

class Materials(models.Model):
    objects = models.Manager()
    MaterialId = models.AutoField(primary_key=True)
    MaterialName = models.CharField(max_length=500)
    Cost = models.CharField(max_length=500)


class Sellers(models.Model):
    objects = models.Manager()
    SellerId = models.AutoField(primary_key=True)
    SellerName = models.CharField(max_length=500)
    Material = models.CharField(max_length=500)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=500)
