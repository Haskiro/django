from rest_framework import serializers
from track.models import Track
from artist.models import Artist

class ArtistSerializerForTrack(serializers.ModelSerializer):
    class Meta:
        model = Artist
        # fields = '__all__'
        fields = ['id', 'nickname']

class TrackSerializer(serializers.ModelSerializer):
    artists_data = ArtistSerializerForTrack(source='artist', many=True)
    class Meta:
        model = Track
        # fields = '__all__'
        exclude = ['artist']
