from django.db import models

# Create your models here.
class PetBreed(models.Model):
    name_breed = models.CharField(max_length=50, verbose_name='name_breed')

    def __str__(self) -> str:
        return self.name_breed
    
    class Meta:
        db_table = 'pets_breed'
        verbose_name_plural ='pets_breed'