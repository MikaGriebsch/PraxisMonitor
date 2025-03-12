from django.db import models


class Patient(models.Model):
    STATUS_CHOICES = [
        ('waiting', 'Wartend'),
        ('in_treatment', 'In Behandlung'),
        ('done', 'Fertig'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='waiting')

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patienten'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"