from . import views
from django.urls import path

app_name = 'addsongs'

urlpatterns = [
    path('addsongs/', views.Songs, name='addsongs'),
    path('addsongs/<int:id>', views.sview, name='sview'),
]


