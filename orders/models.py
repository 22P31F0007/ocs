from django.db import models
from cakes.models import Cake,Category

# Create your models here.
class Order(models.Model):
        caketype = models.CharField(max_length=200)
        quantity = models.CharField(max_length=200)
        address = models.TextField()

def _str_(self):
    return self.name