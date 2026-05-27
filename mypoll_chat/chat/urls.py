from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.index, name='index'),
    path('stream/', views.stream_chat, name='stream_chat'),
]
