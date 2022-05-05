from rest_framework import generics
from core.serializers import EpisodeSerializer, WatchableContentSerializer, HighlightedAreaSerializer
from core.models import Episode, WatchableContent, HighlightedArea

class EpisodeList(generics.ListCreateAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
   
class EpisodeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

class WatchableContentList(generics.ListCreateAPIView):
    queryset = WatchableContent.objects.all()
    serializer_class = WatchableContentSerializer

class WatchableContentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WatchableContent.objects.all()
    serializer_class = WatchableContentSerializer

class HighlightedAreaList(generics.ListCreateAPIView):
    queryset = HighlightedArea.objects.all()
    serializer_class = HighlightedAreaSerializer

class HighlightedAreaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HighlightedArea.objects.all()
    serializer_class = HighlightedAreaSerializer  