from django.db import models
from users.models import User

# Create your models here.

class Activatee(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100,null=True,blank=True)
    surname=models.CharField(max_length=100,null=True,blank=True)
    location=models.CharField(max_length=100,null=True,blank=True)
    proudct_title=models.CharField(max_length=100,null=True,blank=True)
    

    def __str__(self):
        return f'{self.first_name}{self.surname}'

