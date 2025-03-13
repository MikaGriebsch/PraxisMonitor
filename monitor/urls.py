from django.urls import path
from . import views

# In der App-URLs (monitor/urls.py)
app_name = 'monitor'

urlpatterns = [
    path('update_status/', views.update_status, name='update_status'),
    path('active_patient/', views.active_patient, name='active_patient'),  # Name muss genau passen
    path('', views.video_view, name='video_view'),
]