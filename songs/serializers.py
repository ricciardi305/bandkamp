
from rest_framework import serializers

from .models import Song


class SongSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    duration = serializers.IntegerField(required=False)
    album_id = serializers.IntegerField(read_only=True)
    musician_id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return Song.objects.create(**validated_data)
