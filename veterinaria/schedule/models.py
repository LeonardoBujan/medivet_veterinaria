from django.db import models
from turn.models import Turn

# Create your models here.
class Schedule(models.Model):
    id_turn = models.ForeignKey(Turn, on_delete=models.CASCADE)
    date = models.DateField()
    hour = models.TimeField()

    class Meta:
        db_table = 'schedules'
        verbose_name_plural ='schedules'