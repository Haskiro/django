from track.serializers import TrackSerializer
from rest_framework.viewsets import ModelViewSet
from track.models import Track
from django.db.models import Q
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError
from rest_framework.permissions import IsAuthenticated
from authentication.models import UserFavorite
from rest_framework.filters import SearchFilter

# Create your views here.
class TrackViewSet(ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    filterset_fields = ['artist']
    search_fields = ['title']
    filter_backends = (SearchFilter, DjangoFilterBackend)

class GetLatestTwoYearsTracksAPIView(generics.ListAPIView):
    queryset = Track.objects.filter(Q(released_at__year="2023") | Q(released_at__year="2022"))
    serializer_class = TrackSerializer

class ToggleFavoriteTrackViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = UserFavorite.objects.all()
    serializer_class = TrackSerializer
    model = Track

    def list(self, request):
        user = request.user
        user_favs = UserFavorite.objects.get(user=user)
        data = self.serializer_class(user_favs.tracks.all(), many=True).data
        return Response(data)

    def retrieve(self, request, pk=None):
        user = request.user
        user_favs = UserFavorite.objects.get(user=user)

        try:
            self.serializer_class(user_favs.tracks.get(pk=pk)).data
            liked = True
        except self.model.DoesNotExist:
            liked = False

        return Response({'message': liked})

    def create(self, request):
        user = request.user
        if 'trackId' not in request.data or \
                len(request.data.get('trackId')) < 1:
            raise ParseError({'message': 'trackId must not be empty'})

        pk = int(request.data.get('trackId'))
        user_favs = UserFavorite.objects.get(user=user)

        try:
            track = self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise NotFound({'message': 'Track was not found'})

        if track not in user_favs.tracks.all():
            user_favs.tracks.add(track)
        else:
            user_favs.tracks.remove(track)

        user_favs.save()
        return Response({'message': 'success'})

    