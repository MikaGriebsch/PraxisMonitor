from django.contrib import admin
from .models import *

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "status")
    search_fields = ("first_name", "last_name")
    #list_filter = ("status",)
    list_editable = ("status",)
    change_list_template = 'admin/patient_change_list.html'

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