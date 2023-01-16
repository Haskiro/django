from album.serializers import AlbumSerializer
from rest_framework.viewsets import ModelViewSet
from album.models import Album
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

# Create your views here.
class AlbumViewSet(ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    filterset_fields = ['tracks']
    search_fields = ['title']
    filter_backends = (SearchFilter, DjangoFilterBackend)