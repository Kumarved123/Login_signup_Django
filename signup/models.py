from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class Details(models.Model):
   ip_address = models.CharField(max_length = 50,  primary_key=True)
   time_out = models.DateTimeField(default=datetime.now()+timedelta(days=1))
   time_in = models.DateTimeField(auto_now=True)
   attemps = models.IntegerField()

   def __str__(self):
        return self.ip_address