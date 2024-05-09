from django.db import models
from django.contrib.auth.models import User
from pet.models import Pet
from type_attention.models import TypeAttention

# Create your models here.
class Turn(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    id_type_attention = models.ForeignKey(TypeAttention, on_delete=models.CASCADE)

    class Meta:
        db_table = 'turns'
        verbose_name_plural ='turns'