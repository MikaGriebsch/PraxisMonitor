from django.contrib import admin
from .models import Patient, Media 
from django import forms
from django.db import models
from django.contrib import messages
from django.shortcuts import redirect

# Custom Form for PatientAdmin
class PatientAdminForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    form = PatientAdminForm 
    list_display = ("gender", "first_name", "last_name", "status") 
    search_fields = ("gender", "last_name")
    list_editable = ("status",)
    change_list_template = 'admin/patient_change_list.html'
    readonly_fields = ('status_changed',)
    fieldsets = (
        ('Patientenakte', {
            'fields': ('gender', 'first_name', 'last_name', 'status', 'status_changed')
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

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('title', 'media_type', 'display_duration', 'order', 'created_at')
    list_filter = ('media_type', 'created_at')
    search_fields = ('title',)
    ordering = ['order', 'id']
    list_editable = ('order',)
    actions = ['swap_media_order']
    
    fieldsets = (
        ('Medieninformationen', {
            'fields': ('title', 'media_file', 'media_type')
        }),
        ('Anzeigeeinstellungen', {
            'fields': ('display_duration', 'order'),
            'description': 'Anzeigedauer wird nur für Fotos verwendet. Videos verwenden ihre natürliche Länge.'
        }),
    )
    
    def swap_media_order(self, request, queryset):
        """
        Admin-Aktion zum Vertauschen der Reihenfolge von zwei ausgewählten Medien
        """
        if queryset.count() != 2:
            self.message_user(
                request, 
                "Bitte wählen Sie genau zwei Medien zum Vertauschen aus.", 
                level=messages.ERROR
            )
            return
        
        media_list = list(queryset.order_by('order'))
        media1, media2 = media_list[0], media_list[1]
        
        # Tausche die Reihenfolge
        temp_order = media1.order
        media1.order = media2.order
        media2.order = temp_order
        
        media1.save()
        media2.save()
        
        self.message_user(
            request, 
            f'Reihenfolge von "{media1.title}" und "{media2.title}" wurde erfolgreich vertauscht.', 
            level=messages.SUCCESS
        )
    
    swap_media_order.short_description = "Reihenfolge der ausgewählten Medien vertauschen"