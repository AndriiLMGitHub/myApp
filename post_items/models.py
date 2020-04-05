from django.db import models


# Create your models here.
class Add_item(models.Model):
    name_item = models.CharField(max_length=120)
    price_item = models.CharField(max_length=120)
    desciption_item = models.CharField(max_length=120)
