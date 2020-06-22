from django.shortcuts import render, get_object_or_404, redirect
from .models import Song,Artist,Album,GenreAndCategorie
from django.views.generic import ListView, DetailView
import datetime

today = datetime.datetime.now()
last_month = today.month - 1 if today.month>2 else 12
last_month_year = today.year if today.month > last_month else today.year - 1


def HomePage(request):
    return render(request, 'base/base.html')

def LatestSongs(request):
    latest_songs = Song.objects.filter(release_date__year=today.year)
    latest_songs_last_month = Song.objects.filter(release_date__month=last_month)
    return render(request, 'base/list_pages/latest_songs.html', {'latest_songs': latest_songs})

class AllSongsList(ListView):
    model = Song
    template_name = 'base/list_pages/all_songs.html'
    context_object_name = 'all_songs'
    query_pk_and_slug = True

class ArtistList(ListView):
    model =  Artist
    context_object_name = 'all_artists'
    template_name = 'base/list_pages/all_artists.html'
    query_pk_and_slug = True

class GenreAndCategorieList(ListView):
    model = GenreAndCategorie
    context_object_name = 'categorie'
    template_name = 'base/list_pages/categories.html'

class SongDetail(DetailView):
    model = Song
    #album = Song.objects.prefetch_related('album')
    #query_pk_and_slug = True
    template_name = 'base/detail_pages/song.html'
    query_pk_and_slug = True

    def get_queryset(self):
        self.song = get_object_or_404(Song, pk=self.kwargs['pk'],
                                              slug=self.kwargs['slug'])
        
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super(SongDetail, self).get_context_data(**kwargs)
        context['songs_by_artist'] = Song.objects.filter(artist=self.song.artist)
        print(context['songs_by_artist'])
        return context

class ArtistDetail(DetailView):
    model = Artist
    template_name = 'base/detail_pages/artist.html'
    query_pk_and_slug = True

    def get_queryset(self):
        self.artist = get_object_or_404(Artist, pk=self.kwargs['pk'], 
                                                slug=self.kwargs['slug'])
        return super().get_queryset()
    

    def get_context_data(self, **kwargs):
        context = super(ArtistDetail, self).get_context_data(**kwargs)
        context['albums'],context['songs'] = (Album.objects.filter(artist=self.artist), 
                                              Song.objects.filter(artist=self.artist))
        print(context['albums'],context['songs'])
        return context

class AlbumDetail(DetailView):
    model = Album
    template_name = 'base/detail_pages/album.html'
    query_pk_and_slug = True

    def get_queryset(self):
        self.album = get_object_or_404(Album, pk=self.kwargs['pk'],
                                              slug=self.kwargs['slug'])
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super(AlbumDetail, self).get_context_data(**kwargs)
        context['tracks'] = Song.objects.filter(album=self.album)
        print(context['tracks'])
        return context

class ALbumLIst(ListView):
    model = Album
    template_name = 'base/list_pages/albums.html'
    context_object_name = 'albums'
    query_pk_and_slug = True
