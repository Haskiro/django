from track.serializers import TrackSerializer
from rest_framework.viewsets import ModelViewSet
from track.models import Track

# Create your views here.
class TrackViewSet(ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


