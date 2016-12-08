from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(
        max_length = 120,
        null = True,
        blank = True,
    )
    last_name = models.CharField(
        max_length = 120,
        null = True,
        blank = True,
    )

     
