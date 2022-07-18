from albums.models import Album
from albums.serializers import AlbumSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status
from songs.models import Song
from songs.serializers import SongSerializer

from .models import Musician
from .serializers import MusicianSerializer


def get_object_by_id(model, id):
        object = get_object_or_404(model, id=id)

        return object

# Create your views here.
class MusicianView(APIView):
    def get(self, request):
        musicians = Musician.objects.all()

        serializer = MusicianSerializer(musicians, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = MusicianSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

class MusicianDetailView(APIView):
    def get(self, request, musician_id):
        musician = get_object_by_id(Musician, musician_id)

        serializer = MusicianSerializer(musician)

        return Response(serializer.data)

    def patch(self, request, musician_id):
        musician = get_object_by_id(Musician, musician_id)

        serializer = MusicianSerializer(musician, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, musician_id):
        musician = get_object_by_id(Musician, musician_id)

        musician.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class MusicianAlbumView(APIView):
    def get(self, request, musician_id):
        musician = get_object_by_id(Musician ,musician_id)
        albums = Album.objects.filter(musician=musician)

        serializer = AlbumSerializer(albums, many=True)

        return Response(serializer.data)

    def post(self, request, musician_id):
        musician = get_object_by_id(Musician ,musician_id)

        serializer = AlbumSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(musician=musician)

        return Response(serializer.data, status.HTTP_201_CREATED)

class MusicianAlbumSongView(APIView):
    def get(self, request, musician_id, album_id):
        musician = get_object_by_id(Musician ,musician_id)
        album = get_object_by_id(Album, album_id)
        songs = Song.objects.filter(musician=musician, album=album)

        serializer = SongSerializer(songs, many=True)

        return Response(serializer.data)

    def post(self, request, musician_id, album_id):
        musician = get_object_by_id(Musician, musician_id)

        album = Album.objects.filter(musician=musician, id=album_id).first()

        if not album:
            return Response({'detail': 'Album not Found'}, status.HTTP_404_NOT_FOUND)

        serializer = SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(album=album)

        return Response(serializer.data, status.HTTP_201_CREATED)
