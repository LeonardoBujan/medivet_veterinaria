from django.db import models

class TypeAttention(models.Model):
    name_type_attention = models.CharField(max_length=50)

    class Meta:
        db_table = 'types_attention'
        verbose_name_plural ='types_attention'

    
    def __str__(self) -> str:
        return f"{self.name_type_attention}"