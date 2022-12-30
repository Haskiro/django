from genre.serializers import GenreSerializer
from rest_framework.viewsets import ModelViewSet
from genre.models import Genre

# Create your views here.
class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer