from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=11)
    

    
