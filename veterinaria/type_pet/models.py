from django.db import models

class TypePet(models.Model):
    type_pet_name = models.CharField(max_length=30)

    class Meta:
        db_table = 'types_pet'
        verbose_name_plural ='types_pet'


    def __str__(self) -> str:
        return self.type_pet_name

