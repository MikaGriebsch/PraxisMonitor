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
    active_room1 = Patient.objects.filter(status='room1').order_by('-status_changed').first()
    active_room2 = Patient.objects.filter(status='room2').order_by('-status_changed').first()

    response_data = {'active': False}

    if active_room1:
        response_data.update({
            'active': True,
            'room': 'Raum1',
            'id': active_room1.id,
            'name': f"{active_room1.first_name} {active_room1.last_name}",
            'status_changed': active_room1.status_changed.isoformat()
        })
    elif active_room2:
        response_data.update({
            'active': True,
            'room': 'Raum2',
            'id': active_room2.id,
            'name': f"{active_room2.first_name} {active_room2.last_name}",
            'status_changed': active_room2.status_changed.isoformat()
        })

    return JsonResponse(response_data)