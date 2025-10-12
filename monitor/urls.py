from django.urls import path
from . import views

app_name = 'monitor'

urlpatterns = [
    path('update_status/', views.update_status, name='update_status'),
    path('active_patient/', views.active_patient, name='active_patient'), 
    path('', views.media_view, name='media_view'),
]