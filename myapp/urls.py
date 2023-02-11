from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('profile/<str:pk>/', views.userProfile, name='profile'),
    path('create_room/', views.createRoom, name='create-room'),
    path('update_room/<str:pk>/', views.updateRoom, name='update-room'),
    path('delete_room/<str:pk>/', views.deleteRoom, name='delete-room'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('delete_message/<str:pk>/', views.deleteMessage, name='delete-message'),
    path('update-user/', views.updateUser, name='update-user'),
    path('topic/', views.topic, name='topic'),
    path('activity/', views.activity, name='activity'),
]