from rest_framework import serializers
from songs.serializers import SongSerializer

from .models import Album


class AlbumSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    # musician = MusicianSerializer(read_only=True)
    musician_id = serializers.IntegerField(read_only=True)
    total_duration = serializers.SerializerMethodField()
    songs = SongSerializer(many=True, read_only=True)

    def get_total_duration(self, album: Album):
        songs = album.songs.all()
        total_duration = 0
        for song in songs:
            total_duration += song.duration

        # outra forma:
        # from django.db.models import Sum
        # album.songs.aggregate(Sum('duration'))
        return total_duration
    def create(self, validated_data):
        return Album.objects.create(**validated_data)
