from django.db import models
from django.contrib.auth.models import User
class shop(models.Model):
    shop_name=models.CharField(max_length=200)
    own_name=models.CharField(max_length=200)
    address=models.CharField(max_length=300)
    sunday=models.BooleanField()
    start_time=models.TimeField()
    end_time=models.TimeField()
    user=models.ForeignKey(User)
