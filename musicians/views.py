from django.shortcuts import get_object_or_404
from albums.models import Album
from albums.serializers import (
    CreateAlbumSerializer,
    ListAlbumSerializer,
)
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from songs.models import Song
from songs.serializers import ListSongSerializer, CreateSongSerializer

from .models import Musician
from .serializers import (
    CreateMusicianSerializer,
    ListMusicianSerializer,
)
from .mixins import SwitchMethodMixin


# Create your views here.
class MusicianView(SwitchMethodMixin, ListCreateAPIView):

    queryset = Musician.objects.all()
    serializer_map = {"GET": ListMusicianSerializer, "POST": CreateMusicianSerializer}


class MusicianDetailView(SwitchMethodMixin, RetrieveUpdateDestroyAPIView):

    lookup_url_kwarg = "musician_id"

    queryset = Musician.objects.all()
    serializer_map = {
        "GET": ListMusicianSerializer,
        "PATCH": CreateMusicianSerializer,
        "DELETE": CreateMusicianSerializer,
    }


class MusicianAlbumView(SwitchMethodMixin, ListCreateAPIView):

    lookup_url_kwarg = "musician_id"
    queryset = Album.objects.all()
    serializer_map = {"GET": ListAlbumSerializer, "POST": CreateAlbumSerializer}

    def perform_create(self, serializer):
        musician = Musician.objects.get(id=self.kwargs["musician_id"])
        serializer.save(musician=musician)


class MusicianAlbumSongView(SwitchMethodMixin, ListCreateAPIView):

    lookup_url_kwarg = ["musician_id", "album_id"]
    queryset = Song.objects.all()
    serializer_map = {"GET": ListSongSerializer, "POST": CreateSongSerializer}

    def perform_create(self, serializer):
        album = get_object_or_404(Album, pk=self.kwargs["album_id"])
        serializer.save(album=album)
