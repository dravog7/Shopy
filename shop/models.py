from django.db import models
from account.models import shop
# Create your models here.
class announce(models.Model):
    shop = models.ForeignKey(shop,on_delete=models.CASCADE)
    description = models.TextField()