from django.db import models
from pet_owner.models import PetOwner
from pet_breed.models import PetBreed

# Create your models here.
class Pet(models.Model):
    id_pet_owner = models.ForeignKey(PetOwner, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=30)
    id_pet_breed = models.ForeignKey(PetBreed, on_delete=models.CASCADE)
    date_birth_pet = models.DateField()
    weight = models.FloatField()
    height = models.FloatField()

    class Meta:
        db_table = 'pets'
        verbose_name_plural ='pets'