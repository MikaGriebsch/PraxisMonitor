from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/monitor/', include('monitor.urls')),  # Eigenen Namespace erstellen
    path('admin/', admin.site.urls),
]