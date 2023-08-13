from django.db import models
from datetime import datetime
from datetime import date


class appmodel(models.Model):
    name=models.CharField(max_length=30)
    fathername=models.CharField(max_length=30)
    number=models.IntegerField()
    address=models.CharField(max_length=30)
    join=models.DateField(null=True)

    class Meta:
        db_table='APPMODEL'


class Article(models.Model):
    date=models.DateField()
    litre=models.FloatField(max_length=100,)
    rate=models.FloatField(max_length=100,)
    vendor=models.ForeignKey(appmodel,on_delete=models.CASCADE)
    name=models.CharField(max_length=30,null=True)

    
    



    
# Create your models here.
