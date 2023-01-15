from genre.serializers import GenreSerializer
from rest_framework.viewsets import ModelViewSet
from genre.models import Genre
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']