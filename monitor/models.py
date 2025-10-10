from django.db import models
from django.utils import timezone

class Patient(models.Model):
    STATUS_CHOICES = [
        ('absend', 'Abwesend'), # Korrigiert von Abwehsend
        ('waiting', 'Wartend'),
        ('room1', 'Raum 1'),
        ('room2', 'Raum 2'),
        ('done', 'Fertig'),
    ]

    first_name = models.CharField(max_length=50, verbose_name="Vorname")
    last_name = models.CharField(max_length=50, verbose_name="Nachname")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='waiting', verbose_name="Status")
    status_changed = models.DateTimeField(auto_now_add=True, verbose_name="Status geändert am")
    last_treatment_notes = models.TextField(blank=True, null=True, verbose_name="Letzte Behandlungsnotizen")

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patienten'
        unique_together = (('first_name', 'last_name'),)

    def save(self, *args, **kwargs):
        if self.pk:
            orig = Patient.objects.get(pk=self.pk)
            if orig.status != self.status:
                self.status_changed = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class PatientHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='history_entries', verbose_name="Patient")
    visit_date = models.DateTimeField(default=timezone.now, verbose_name="Besuchsdatum")
    notes = models.TextField(verbose_name="Notizen")

    class Meta:
        verbose_name = 'Historie Eintrag'
        verbose_name_plural = 'Historie Einträge'
        ordering = ['-visit_date']

    def __str__(self):
        return f"Eintrag für {self.patient} am {self.visit_date.strftime('%Y-%m-%d %H:%M')}"


class Media(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('video', 'Video'),
        ('photo', 'Foto'),
    ]
    
    title = models.CharField(max_length=100, verbose_name="Titel")
    media_file = models.FileField(upload_to='media/', verbose_name="Mediendatei")
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES, default='video', verbose_name="Medientyp")
    display_duration = models.PositiveIntegerField(default=10, help_text="Anzeigedauer in Sekunden (nur für Fotos)", verbose_name="Anzeigedauer")
    order = models.PositiveIntegerField(blank=True, null=True, verbose_name="Reihenfolge")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Erstellt am")

    class Meta:
        verbose_name = 'Medium'
        verbose_name_plural = 'Medien'
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.title} ({self.get_media_type_display()})"
    
    def save(self, *args, **kwargs):
        if self.order is None:
            # Setze die Reihenfolge automatisch als nächste verfügbare Nummer
            last_order = Media.objects.aggregate(models.Max('order'))['order__max']
            self.order = (last_order or 0) + 1
        super().save(*args, **kwargs)