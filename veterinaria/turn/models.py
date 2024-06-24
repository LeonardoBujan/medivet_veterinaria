from django.db import models
from pet.models import Pet
from professional.models import Professional
from django.contrib.auth.models import User

class Turn(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        db_table = 'turns'
        verbose_name_plural ='turns'