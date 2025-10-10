from django.urls import path
from . import views

app_name = 'monitor'

urlpatterns = [
    path('update_status/', views.update_status, name='update_status'),
    path('update_status_with_notes/', views.update_status_with_notes, name='update_status_with_notes'), 
    path('active_patient/', views.active_patient, name='active_patient'), 
    path('', views.media_view, name='media_view'),
]