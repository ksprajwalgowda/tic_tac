from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime    

# Create your models here.
class UserDetails(models.Model):
    email = models.EmailField(max_length = 254,unique=True,null=False)
    username = models.CharField(max_length=254,unique=True,null=False,default='')
    first_name = models.CharField(max_length=30,null=False)  
    last_name = models.CharField(max_length=30,null=False)  
    dob = models.DateField(null=False)
    gender = models.CharField(max_length=10,null=False)
    bio = models.TextField(null=True)
    phoneNumberRegex = RegexValidator(regex = r"\d{10}")
    phone_no =  models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
    profile_image = models.ImageField(upload_to='profile_pic/',blank=True)
    updated_time = models.DateTimeField(default=datetime.now, blank=True)