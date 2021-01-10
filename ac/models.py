from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    DOB = models.DateField(default=datetime.now)
    company = models.CharField(max_length=50)
# Create your models here.
