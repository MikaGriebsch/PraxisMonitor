from django.db import models
from django.utils import timezone

class Patient(models.Model):
    STATUS_CHOICES = [
        ('absend', 'Abwehsend'),
        ('waiting', 'Wartend'),
        ('room1', 'Raum 1'),
        ('room2', 'Raum 2'),
        #('in_treatment', 'In Behandlung'),
        ('done', 'Fertig'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='waiting')
    status_changed = models.DateTimeField(auto_now_add=True)  # Neues Feld

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patienten'

    def save(self, *args, **kwargs):
        """Aktualisiert den status_changed Zeitstempel bei Statusänderung"""
        if self.pk:  # Nur bei Updates prüfen
            orig = Patient.objects.get(pk=self.pk)
            if orig.status != self.status:
                self.status_changed = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Video(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title