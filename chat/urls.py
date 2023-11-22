from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("", views.chat_room, name="index"),
    path("<str:room_name>/", views.room, name="room"),
]
