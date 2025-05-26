from django.core.management.base import BaseCommand
from django.utils import timezone
from monitor.models import Patient

class Command(BaseCommand):
    help = 'Ändert den Status von "done" zu "absend" nach 2 Minuten'

    def handle(self, *args, **kwargs):
        patients = Patient.objects.filter(status='done')
        cutoff_time = timezone.now() - timezone.timedelta(minutes=2)

        for patient in patients:
            if patient.status_changed <= cutoff_time:
                patient.status = 'absend'
                patient.save()
                self.stdout.write(f"Patient {patient.id} auf 'absend' gesetzt.")