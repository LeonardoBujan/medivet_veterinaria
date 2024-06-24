from django.db import models
from django.contrib.auth.models import User
from type_pet.models import TypePet

class Pet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type_pet = models.ForeignKey(TypePet, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=30)
    date_birth_pet = models.DateField()

    class Meta:
        db_table = 'pets'
        verbose_name_plural ='pets'

    def __str__(self) -> str:
        return self.pet_name

    