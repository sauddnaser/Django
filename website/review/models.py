from django.db import models
from django.contrib.auth.models import User
from startingwebsite.models import Tea

class Rev(models.Model):
    Name = models.CharField(max_length=255, null=True)
    Email = models.CharField(max_length=255, null=True)
    Title = models.CharField(max_length=255, null=True)
    write = models.CharField(max_length=500, null=True)
    Product = models.ForeignKey(Tea, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.Title