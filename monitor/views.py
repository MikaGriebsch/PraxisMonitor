from django.shortcuts import render
from django.http import JsonResponse
from .models import Patient
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required

def index_view(request):
    return render(request, 'index.html')
# views.py

def update_status(request):
    if request.method == 'POST':
        patient_id = request.POST.get('id')
        new_status = request.POST.get('status')
        patient = Patient.objects.get(id=patient_id)
        patient.status = new_status
        patient.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.admin.views.decorators import staff_member_required
import json

@staff_member_required
@require_http_methods(["POST"])
def update_status(request):
    try:
        data = json.loads(request.body)
        patient = Patient.objects.get(id=data['id'])
        patient.status = data['status']
        patient.save()
        return JsonResponse({'status': 'success'})
    except Patient.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Patient nicht gefunden'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)