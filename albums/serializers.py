from rest_framework import serializers
from songs.serializers import ListSongSerializer
from django.db.models import Sum

from .models import Album


class CreateAlbumSerializer(serializers.ModelSerializer):
    songs = ListSongSerializer(many=True, read_only=True)
    total_duration = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = "__all__"
        extra_kwargs = {"musician": {"read_only": True}}

    def get_total_duration(self, album: Album):
        return album.songs.aggregate(Sum("duration"))


class ListAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"
