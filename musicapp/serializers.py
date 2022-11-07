from rest_framework import serializers
from .models import Artiste, Song, Lyrics

class ArtisteSerializer( serializers.ModelSerializer):
    class Meta:
        model= Artiste
        fields=['first_name', 'last_name', 'age']


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model= Song
        fields=['Artist_id', 'title', 'date_released','likes']

class LyricsSerializer( serializers.ModelSerializer):
    class Meta:
        model= Lyrics
        fields=['song_id', 'content']

