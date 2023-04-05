from django.db import models

# Create your models here.

class home(models.Model):
    homename=models.CharField(max_length=100)
    homedescription=models.TextField()
class room(models.Model):
    roomname=models.CharField(max_length=100)
    roomdiscription=models.TextField()
    

