from django.db import models
from users.models import User
# Create your models here.

class Donoractive(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.name

