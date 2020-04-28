from django.db import models

# Create your models here.
class Calculates(models.Model):
    name_calculates = models.CharField(max_length = 50)
    color = models.CharField(max_length = 50)
    description = models.TextField(max_length = 300)
    date = models.DateTimeField()
