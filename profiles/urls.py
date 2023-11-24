from django.urls import path
from . import views

urlpatterns = [
  path('<int:pk>/profiledetail/', views.DisplayProfile.as_view(), name='profile'),
  path(
    'register/', views.Registration.as_view(), name='register'),
  path('profile_list/', views.ProfileList.as_view(), name='profile_list'),
]