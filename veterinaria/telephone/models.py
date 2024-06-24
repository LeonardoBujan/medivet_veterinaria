from django.db import models
from django.contrib.auth.models import User

class Telephone(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country_code = models.CharField(max_length=5)
    area_code = models.CharField(max_length=10)
    telephone_number = models.CharField(max_length=15)

    class Meta:
        db_table = 'telephones'
        verbose_name_plural = 'telephones'
