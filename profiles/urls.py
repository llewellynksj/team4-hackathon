from django.urls import path
from . import views

urlpatterns = [
  path('', views.display_profile, name='profile'),
  path(
    'register/',
    views.Registration.as_view(),
    name='register'),
]