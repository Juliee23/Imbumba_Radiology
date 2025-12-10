from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('appointments/', views.appointments, name='appointments'),
    path('appointments-success/', views.appointments_success, name='appointments_success'),
    path('contact/', views.contact, name='contact'),

]

