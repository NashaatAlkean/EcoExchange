from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email=models.EmailField(unique=True)
    is_donor=models.BooleanField(default=False)
    is_seeker=models.BooleanField(default=False)
    # to_activate_seeker=models.BooleanField(default=False)
    # to_activate_donor=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)


