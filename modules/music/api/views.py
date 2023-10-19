# Create your views here.
from ..models import Music
from .serializers import MusicSerializer

from rest_framework import viewsets


# Create your views here.
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    http_method_names = ['get', 'post', 'patch']