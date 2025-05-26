from django.contrib import admin
from .models import Patient, PatientHistory, Video 
from django import forms
from django.db import models

# Custom Form for PatientAdmin
class PatientAdminForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'last_treatment_notes': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        }

# Admin-Interface für Patientenhistorie
class PatientHistoryInline(admin.TabularInline):
    model = PatientHistory
    extra = 0  
    fields = ('visit_date', 'notes')
    readonly_fields = ('visit_date',)
    can_delete = False 
    ordering = ('-visit_date',)
    formfield_overrides = {
        models.TextField: {'widget': forms.Textarea(attrs={'rows':4, 'cols':40})}, #Hier die Höhe der Notes-Felder anpassen
    }

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    form = PatientAdminForm 
    list_display = ("first_name", "last_name", "status", "last_treatment_notes") 
    search_fields = ("first_name", "last_name")
    list_editable = ("status",)
    change_list_template = 'admin/patient_change_list.html'
    inlines = [PatientHistoryInline]
    readonly_fields = ('status_changed',)
    fieldsets = (
        ('Patientenakte', {
            'fields': ('first_name', 'last_name', 'status', 'status_changed', 'last_treatment_notes') # status_changed hinzugefügt
        }),
    )

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context.update({
            'waiting': Patient.objects.filter(status='waiting'),
            'room1': Patient.objects.filter(status='room1'),
            'room2': Patient.objects.filter(status='room2'),
            'done': Patient.objects.filter(status='done'),
        })
        return super().changelist_view(request, extra_context=extra_context)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')