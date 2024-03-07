from django.db import models
from users.models import User
# Create your models here.

class Items(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    descreption=models.TextField()
    #image=models.ImageField(default='',upload_to='img/%y')
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return self.title

