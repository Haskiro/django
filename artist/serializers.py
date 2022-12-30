from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from artist.models import Artist
from track.models import Track
from album.models import Album
from track.serializers import TrackSerializer

class AlbumSerializerForArtist(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'title', 'cover']


class ArtistSerializer(serializers.ModelSerializer):
    tracks_data = TrackSerializer(source='tracks', many=True)
    albums_data = AlbumSerializerForArtist(source='albums', many=True)
    class Meta:
        model = Artist
        fields = '__all__'
