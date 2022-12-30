from rest_framework.viewsets import ModelViewSet
from artist.serializers import ArtistSerializer
from artist.models import Artist

class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
