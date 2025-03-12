from django.db import models

class Patient (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patienten'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
