from django.db import models
from type_attention.models import TypeAttention

class Professional (models.Model):
    first_name_professional = models.CharField(max_length=50)
    last_name_professional = models.CharField(max_length=50)
    registration = models.CharField(max_length=20)
    type_attention = models.ForeignKey(TypeAttention, on_delete=models.CASCADE)

    class Meta:
        db_table = 'professional'
        verbose_name_plural = 'professionals'

    def __str__(self) -> str:
        return f"{self.first_name_professional} {self.last_name_professional}"

