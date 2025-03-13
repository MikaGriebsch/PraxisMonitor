from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.admin.views.decorators import staff_member_required
import json
from django.shortcuts import render
from .models import Video, Patient

@staff_member_required
@require_http_methods(["POST"])
def update_status(request):
    try:
        data = json.loads(request.body)
        patient = Patient.objects.get(id=data['id'])
        old_status = patient.status
        patient.status = data['status']
        patient.save()
        return JsonResponse({
            'status': 'success',
            'new_status': patient.status,
            'new_status_display': patient.get_status_display()
        })
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

def video_view(request):
    videos = Video.objects.all()
    return render(request, 'video_player.html', {'videos': videos})


def active_patient(request):
    # Holt den neuesten Patienten mit Statusänderung
    #active = Patient.objects.filter(status='in_treatment').order_by('-id').first()
    active = Patient.objects.filter(status='in_treatment').order_by('-status_changed').first()

    if active:
        return JsonResponse({
            'active': True,
            'id': active.id,
            'name': f"{active.first_name} {active.last_name}",
            'status_changed': active.status_changed  # Neues Feld benötigt!
        })
    return JsonResponse({'active': False})