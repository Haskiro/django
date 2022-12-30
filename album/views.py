from album.serializers import AlbumSerializer
from rest_framework.viewsets import ModelViewSet
from album.models import Album

# Create your views here.
class AlbumViewSet(ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()