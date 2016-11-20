from django.db import models

# Create your models here.
class Engineer(models.Model):
    first_name = models.CharField(
        max_length=120,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=120,
        null=True,
        blank=True,
    )
    company = models.CharField(
        max_length=120,
        null=True,
        blank=True,
    )
    email = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    phone = models.CharField(
        max_length=10,

    )

    def __str__(self):
        return self.first_name + self.last_name


