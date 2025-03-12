from django.contrib import admin
from .models import Patient
from django.utils.html import format_html
from django.urls import path
from django.shortcuts import render


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "status_column")
    search_fields = ("first_name", "last_name")

    # Neue Methoden für die Drag & Drop-Ansicht
    change_list_template = 'admin/patient_change_list.html'

    def status_column(self, obj):
        return format_html('<div class="status-cell" data-id="{}">{}</div>', obj.id, obj.get_status_display())

    status_column.short_description = 'Status'

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['waiting'] = Patient.objects.filter(status='waiting')
        extra_context['in_treatment'] = Patient.objects.filter(status='in_treatment')
        extra_context['done'] = Patient.objects.filter(status='done')
        return super().changelist_view(request, extra_context=extra_context)