from django.views.decorators.http import require_http_methods
from . import views
from django.urls import path, re_path
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index_view, name='index_view'),
    #path('admin/update_status/', views.update_status, name='update_status'),
    path('admin/update_status/', require_http_methods(['POST'])(views.update_status), name='update_status'),
    path('update_status/', views.update_status, name='update_status'),

]