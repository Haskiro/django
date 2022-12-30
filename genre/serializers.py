from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from genre.models import Genre
from track.serializers import TrackSerializer

class GenreSerializer(serializers.ModelSerializer):
    tracks_data = TrackSerializer(source='tracks', many=True)
    class Meta:
        model = Genre
        exclude = ['tracks']