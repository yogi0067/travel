from django.db import models

# Create your models here.

class Destination(models.Model):

    destName = models.CharField(max_length=100,default='')
    destPrice = models.IntegerField()
    destDesc = models.TextField(default='')
    destImage = models.ImageField(upload_to='images')
    destOffer = models.BooleanField(default=False)
