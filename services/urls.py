from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_list, name='service_list'),
    path('add_service/', views.add_service, name='add_service'),
    path('edit/<int:service_id>/', views.edit_service, name='edit_service'),
    path('delete/<int:service_id>/', views.delete_service, name='delete_service'),
]
