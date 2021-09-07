from django.db import models

# Create your models here.

class Survey(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    pregnancy = models.CharField(max_length=20)
    marital = models.CharField(max_length=20)
    diet = models.CharField(max_length=20)
    ratefollow = models.CharField(max_length=20)
    rate=models.CharField(max_length=10)
    class Meta:
         db_table = "survey"



