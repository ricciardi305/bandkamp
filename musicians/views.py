from albums.models import Album
from albums.serializers import (
    CreateAlbumSerializer,
    ListAlbumSerializer,
)
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from songs.models import Song
from songs.serializers import SongSerializer

from .models import Musician
from .serializers import (
    CreateMusicianSerializer,
    ListMusicianSerializer,
)
from .mixins import SwitchMethodMixin


def get_object_by_id(model, id):
    object = get_object_or_404(model, id=id)

    return object


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


class MusicianAlbumSongView(APIView):
    def get(self, request, musician_id, album_id):
        musician = get_object_by_id(Musician, musician_id)
        album = get_object_by_id(Album, album_id)
        songs = Song.objects.filter(musician=musician, album=album)

        serializer = SongSerializer(songs, many=True)

        return Response(serializer.data)

    def post(self, request, musician_id, album_id):
        musician = get_object_by_id(Musician, musician_id)

        album = Album.objects.filter(musician=musician, id=album_id).first()

        if not album:
            return Response({"detail": "Album not Found"}, status.HTTP_404_NOT_FOUND)

        serializer = SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(album=album)

        return Response(serializer.data, status.HTTP_201_CREATED)
