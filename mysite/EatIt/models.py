from django.db import models
from . import choices
# Create your models here.
class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length= 20)
    health_value = models.IntegerField(default = 0)
    alcohol = models.BooleanField(default = False)
    image = models.ImageField()
    distance = models.DecimalField(decimal_places= 2, max_digits=10)
    price = models.DecimalField(decimal_places= 2, max_digits=10)
class Search(models.Model):
    health_choice = models.CharField(choices =choices.HEALTH_CHOICES)