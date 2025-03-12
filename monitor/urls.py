from django.urls import path
from . import views

app_name = 'monitor'  # Namespace hinzufügen

urlpatterns = [
    path('update_status/', views.update_status, name='update_status'),
]