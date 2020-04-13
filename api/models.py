from django.db import models


class ResourceModel(models.Model):
    title = models.CharField(max_length=255)
    amount = models.IntegerField()
    measure = models.CharField(max_length=50)
    price = models.FloatField()
    date = models.DateField()
