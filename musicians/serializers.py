from rest_framework import serializers
from albums.serializers import ListAlbumSerializer
from .models import Musician

class CreateMusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = "__all__"

class ListMusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = "__all__"