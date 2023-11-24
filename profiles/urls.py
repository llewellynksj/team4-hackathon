from django.urls import path, include
from . import views

urlpatterns = [
  path('<int:pk>/profiledetail/', views.display_profile, name='profile'),
  path('register/', views.Registration.as_view(), name='register'),
  path('profile_list/', views.ProfileList.as_view(), name='profile_list'),
  path('<int:pk>/update_profile', views.UpdateProfile.as_view(), name='update_profile'),
  path('', include('chat.urls'), name='chat')
]