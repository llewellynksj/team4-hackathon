from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("", views.index, name="index"),
    path('<int:profile_id>/profiledetail/rooms/<int:pk>', views.rooms, name='rooms'),
    # path('<str:room>/', views.room, name='room'),
    # path('checkview', views.checkview, name='checkview'),
    # path('send', views.send, name='send'),
    # path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]
