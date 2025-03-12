from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "get_status_display")
    list_filter = ("status",)
    change_list_template = 'admin/patient_change_list.html'

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context.update({
            'waiting': Patient.objects.filter(status='waiting'),
            'in_treatment': Patient.objects.filter(status='in_treatment'),
            'done': Patient.objects.filter(status='done'),
        })
        return super().changelist_view(request, extra_context=extra_context)