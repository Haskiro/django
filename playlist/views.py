from playlist.serializers import PlaylistSerializer
from playlist.models import Playlist
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class PlaylistViewSet(ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

# class PlaylistPagination(PageNumberPagination):
#     page_size = 100
#     page_size_query_param = 'page_size'
#     max_page_size = 1000