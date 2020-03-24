from django.db import models

# Create your models here.

class Articles(models.Model):
    name_good = models.CharField(max_length = 50)
    price = models.IntegerField()
    description = models.TextField(max_length = 300)
    date = models.DateTimeField()

    def __str__(self):
        return self.name_good
