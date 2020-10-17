from django.shortcuts import render
from django.http import HttpResponse
from addsongs.models import Song


def Songs(request):
    song = Song.objects.all()
    return render(request, "addsongs/base.html", {"song": song})


def sview(request, id):
    song = Song.objects.filter(song_id=id).first()
    return render(request, "addsongs/play.html", {"song": song})
