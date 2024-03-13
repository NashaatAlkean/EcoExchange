from django.db import models
from users.models import User
import datetime
# Create your models here.

class Items(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    descreption=models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    is_available=models.BooleanField(default=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class RequestsItems(models.Model):
    status_choices=(('Accepted','Accepted'),('Decliened','Decliened'))
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    item=models.ForeignKey(Items,on_delete=models.CASCADE)
    timestamp=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=20,choices=status_choices)