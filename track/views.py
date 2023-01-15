from track.serializers import TrackSerializer
from rest_framework.viewsets import ModelViewSet
from track.models import Track
from django.db.models import Q
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class TrackViewSet(ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class GetLatestTwoYearsTracksAPIView(generics.ListAPIView):
    queryset = Track.objects.filter(Q(released_at__year="2023") | Q(released_at__year="2022"))
    serializer_class = TrackSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']
