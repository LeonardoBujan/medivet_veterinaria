from django.db import models
from django.contrib.auth.models import User
from type_pet.models import TypePet

class Pet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    type_pet = models.ForeignKey(TypePet, on_delete=models.CASCADE, null=False)
    pet_name = models.CharField(max_length=30, null=False)
    date_birth_pet = models.DateField()
    image_pet = models.ImageField(upload_to='pets', null=True, blank=True)

    class Meta:
        db_table = 'pets'
        verbose_name_plural ='pets'

    def __str__(self) -> str:
        return self.pet_name

    