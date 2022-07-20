from rest_framework import serializers
from .models import Song


class ListSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"


class CreateSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"
        extra_kwargs = {"album": {"read_only": True}}
