from rest_framework.viewsets import ModelViewSet
from artist.serializers import ArtistSerializer
from artist.models import Artist
from django_filters.rest_framework import DjangoFilterBackend

class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nickname']
