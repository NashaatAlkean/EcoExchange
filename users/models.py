from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
# Create your models here.

class User(AbstractUser):
    email=models.EmailField(unique=True)
    is_donor=models.BooleanField(default=False)
    is_seeker=models.BooleanField(default=False)
    # to_activate_seeker=models.BooleanField(default=False)
    # to_activate_donor=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    date_modified=models.DateTimeField(User,auto_now=True)
    def __str__(self):
        return self.user.email
    
    

#create profile for  new user
    

def create_profile(sender,instance,created,**kwargs):
    if created:
        user_profile=Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile,sender=User)
