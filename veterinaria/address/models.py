from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=50)
    number = models.CharField(max_length=10)
    floor = models.CharField(max_length=5)
    deparment = models.CharField(max_length=5)

    class Meta:
        db_table = 'address'
        verbose_name_plural ='address'
