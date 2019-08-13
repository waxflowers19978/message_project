from django.urls import path
from . import views

app_name = 'message'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('index/', views.index, name = 'index'),
    path('<str:room_name>/', views.room, name='room'),
]
