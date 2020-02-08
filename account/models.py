from django.db import models
from django.contrib.auth.models import User
from datetime import time
defaulttime=time(0,00)
class shop(models.Model):
    shop_name=models.CharField(max_length=200)
    own_name=models.CharField(max_length=200)

    address=models.CharField(max_length=300)
    latitude=models.IntegerField()
    longtitude=models.IntegerField()

    sunday=models.BooleanField()
    start_time=models.TimeField()
    end_time=models.TimeField()
    curr_start=models.TimeField(default=defaulttime) #add default
    curr_end=models.TimeField(default=defaulttime)
    open=models.BooleanField(default=False)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='shop')