from rest_framework import serializers
from songs.serializers import ListSongSerializer
from django.db.models import Sum

from .models import Album


class CreateAlbumSerializer(serializers.ModelSerializer):
    songs = ListSongSerializer(many=True, read_only=True)
    total_duration = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = ["id", "songs", "total_duration", "name", "musician"]
        extra_kwargs = {"musician": {"read_only": True}}

    def get_total_duration(self, obj) -> dict:
        return obj.songs.aggregate(Sum("duration"))


class ListAlbumSerializer(serializers.ModelSerializer):
    quantity_songs = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = "__all__"

    def get_quantity_songs(self, obj) -> int:
        return obj.songs.count()
