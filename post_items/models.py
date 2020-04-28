from django.db import models


# Create your models here.
class Add_item(models.Model):
    name_item = models.CharField(max_length=120)
    price_item = models.CharField(max_length=120)
    desciption_item = models.CharField(max_length=120)
    document = models.FileField(upload_to='documents/')
    model_pic = models.ImageField(upload_to = 'pic_folder/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
