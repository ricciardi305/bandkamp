from django.db import models


# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=255)
    duration = models.IntegerField(null=True)

    album = models.ForeignKey(
        "albums.Album", on_delete=models.CASCADE, related_name="songs"
    )
