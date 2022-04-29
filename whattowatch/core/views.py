from rest_framework import viewsets
from core.serializers import EpisodeSerializer, WatchableContentSerializer, HighlightedAreaSerializer
from core.models import Episode, WatchableContent, HighlightedArea

class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

class WatchableContentViewSet(viewsets.ModelViewSet):
    queryset = WatchableContent.objects.all()
    serializer_class = WatchableContentSerializer

class HighlightedAreaViewSet(viewsets.ModelViewSet):
    queryset = HighlightedArea.objects.all()
    serializer_class = HighlightedAreaSerializer
    