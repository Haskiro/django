from rest_framework.viewsets import ModelViewSet
from artist.serializers import ArtistSerializer
from artist.models import Artist
from rest_framework.filters import SearchFilter

class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    search_fields = ['nickname']
    filter_backends = (SearchFilter,)
