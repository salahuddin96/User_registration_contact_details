
from django.db import models

# Create your models here.

class User_Registarion(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    class Meta:
        db_table='user'

class Login(models.Model):
    user = models.ForeignKey(User_Registarion, on_delete=models.CASCADE, null=True, blank=True)
    contact_1= models.CharField(max_length=50)
    contact_2 = models.CharField(max_length=50)

    class Meta:
        db_table='login'