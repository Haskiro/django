from playlist.serializers import PlaylistSerializer
from playlist.models import Playlist
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from track.models import Track


class PlaylistViewSetPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 8

# Create your views here.
class PlaylistViewSet(ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    pagination_class = PlaylistViewSetPagination
    filterset_fields = ['tracks']
    search_fields = ['title']
    filter_backends = (SearchFilter, DjangoFilterBackend)

    @action(methods=['POST'], detail=True,
        permission_classes=[IsAuthenticated])
    def add_track_to_playlist(self, request, pk=None):
        user = request.user
        print(user)
        data = request.data
        playlist = Playlist.objects.get(pk=pk)
        for playlist_id in data:
            track = Track.objects.get(id=playlist_id)
            playlist.tracks.add(track);
        playlist.save()

        return Response({'message': "track added"})
    