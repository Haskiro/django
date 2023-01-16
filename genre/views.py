from genre.serializers import GenreSerializer
from rest_framework.viewsets import ModelViewSet
from genre.models import Genre
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

# Create your views here.
class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filterset_fields = ['tracks']
    search_fields = ['title']
    filter_backends = (SearchFilter, DjangoFilterBackend)