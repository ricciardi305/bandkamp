from albums.serializers import AlbumSerializer
from rest_framework import serializers

from .models import Musician

class CreateMusicianSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True, read_only=True)
    class Meta:
        model = Musician
        fields = "__all__"

class ListMusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = "__all__"