from playlist.serializers import PlaylistSerializer
from playlist.models import Playlist
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination


class PlaylistViewSetPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 8

# Create your views here.
class PlaylistViewSet(ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    pagination_class = PlaylistViewSetPagination