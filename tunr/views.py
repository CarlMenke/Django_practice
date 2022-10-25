from django.shortcuts import render

# Create your views here.

from .models import Artist, Song

def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'tunr/artist_list.html', {"artist":artists})

def song_list(request):
    songs = Song.objects.all()
    return render(request,'tunr/song_list.html', {'songs':songs})

def artist_detail(request, pk):
    artist = Artist.objects.get(id=pk)
    return render(request, 'tunr/artist_details.html', {'artist', artist})
