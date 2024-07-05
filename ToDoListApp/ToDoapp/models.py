from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class tasks(models.Model):  
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    task = models.CharField(max_length=90)
    status= models.BooleanField(default=False)