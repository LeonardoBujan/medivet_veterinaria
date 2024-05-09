from django.db import models

# Create your models here.
class PetOwner(models.Model):
    document_number = models.IntegerField()
    date_birth_owner = models.DateField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=50)

    class Meta:
        db_table = 'pets_owner'
        verbose_name_plural ='pets_owner'