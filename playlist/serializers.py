from rest_framework import serializers
from playlist.models import Playlist
from track.serializers import TrackSerializer

class PlaylistSerializer(serializers.ModelSerializer):
    tracks_data = TrackSerializer(source='tracks', many=True)
    class Meta:
        model = Playlist
        exclude = ['tracks']