from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_home, name='home'),
    path('team/', views.display_team, name='team'),
    path('contact/', views.display_contact, name='contact'),
]
