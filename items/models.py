from django.db import models
from users.models import User
import datetime
# Create your models here.

class City(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

class Catagory(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Items(models.Model):
    item_type_choices=(
        ('New','New'),
        ('Like New','Like New'),
        ('Good','Good'),
        ('Fair','Fair'),
        ('Acceptable','Acceptable'),
        ('Well-loved','Well-loved'),
        ('Damaged','Damaged'),
        ('Broken','Brokens'),



    )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    descreption=models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    is_available=models.BooleanField(default=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    catagory=models.ForeignKey(Catagory,on_delete=models.DO_NOTHING, null=True, blank=True)
    city=models.ForeignKey(City,on_delete=models.DO_NOTHING, null=True, blank=True)
    item_type=models.CharField(max_length=20,choices=item_type_choices,null=True)
    is_approved=models.BooleanField(default=False) # whether aproved by admin to show it for searchers or not



    def __str__(self):
        return self.title


class RequestsItems(models.Model):
    status_choices=(('Accepted','Accepted'),('Decliened','Decliened'))
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    item=models.ForeignKey(Items,on_delete=models.CASCADE)
    timestamp=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=20,choices=status_choices)