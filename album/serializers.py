from dataclasses import fields
from rest_framework import serializers
from album.models import Album
from track.serializers import TrackSerializer

class  AlbumSerializer(serializers.ModelSerializer):
    tracks_data = TrackSerializer(source='tracks', many=True)
    class Meta:
        model = Album
        exclude = ['artist', 'tracks']
