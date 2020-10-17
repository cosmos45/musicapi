from django.shortcuts import render
from .models import Playlists
from addsongs.models import Song
from django.db.models import Case, When


def playlists(request):
    if request.method == "POST":
        user = request.user
        video_id = request.POST['video_id']
        play = Playlists.objects.filter(user=user)
        for i in play:
            if video_id == i.video_id:
                message = "This song is Already added"
                break
        else:
            playlists = Playlists(user=user, video_id=video_id)
            playlists.save()
            message = "This song is Succesfully added"

        song = Song.objects.filter(song_id=video_id).first()
        return render(request, "addsongs/play.html", {"song": song, "message": message})

    pl = Playlists.objects.filter(user=request.user)
    ids = []
    for i in pl:
        ids.append(i.video_id)

    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    song = Song.objects.filter(song_id__in=ids).order_by(preserved)

    return render(request, "playlists/playlist.html", {'song': song})
