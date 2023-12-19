from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tea(models.Model):
    Name=models.CharField(max_length=255,null=True)
    Grade=models.CharField(max_length=255,null=True)
    Country=models.CharField(max_length=255,null=True)
    Price=models.CharField(max_length=255,null=True)
    details=models.CharField(max_length=500,null=True)
    In_stock =models.CharField(max_length=255,null=True)
    image=models.ImageField(upload_to='Tea_images/',null=True)
    
    def __str__(self):
        return self.Name + ' ' + self.Grade