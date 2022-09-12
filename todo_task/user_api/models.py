from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    mobile = models.CharField(max_length=10,blank=False,null=False) # We can send notification on mobile nmber
    mobile_number_verified = models.BooleanField(default=False)

    

