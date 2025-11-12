from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_views, name='home'),
    path('about/', views.about_views, name='about'),
    path('contact/', views.contact_views, name='contact'),
    path('booking/', views.booking_views, name='booking'),
    path('doctors/', views.doctors_views, name='doctors'),
    path('department/', views.department_views, name='department'),
    path('confirmation/', views.confirmation_views, name='confirmation'),
]
