from django.urls import path
from . import views

app_name = 'playlists'


urlpatterns = [

    path('playlists/', views.playlists, name='playlists')
]