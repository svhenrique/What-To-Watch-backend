from rest_framework import generics
from core.serializers import EpisodeSerializer, WatchableContentSerializer, HighlightedAreaSerializer
from core.models import Episode, WatchableContent, HighlightedArea
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class EpisodeRead(generics.RetrieveAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

class EpisodeList(generics.ListAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

class EpisodeCreate(generics.CreateAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )

class EpisodeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )

class WatchableContentRead(generics.RetrieveAPIView):
    queryset = WatchableContent.objects.all()
    serializer_class = WatchableContentSerializer

class WatchableContentList(generics.ListAPIView):
    queryset = WatchableContent.objects.all()
    serializer_class = WatchableContentSerializer

class WatchableContentCreate(generics.CreateAPIView):
    queryset = WatchableContent.objects.all()
    serializer_class = WatchableContentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )

class WatchableContentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WatchableContent.objects.all()
    serializer_class = WatchableContentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )

class HighlightedAreaRead(generics.RetrieveAPIView):
    queryset = HighlightedArea.objects.all()
    serializer_class = HighlightedAreaSerializer  

class HighlightedAreaList(generics.ListAPIView):
    queryset = HighlightedArea.objects.all()
    serializer_class = HighlightedAreaSerializer  

class HighlightedAreaCreate(generics.CreateAPIView):
    queryset = HighlightedArea.objects.all()
    serializer_class = HighlightedAreaSerializer  
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )

class HighlightedAreaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HighlightedArea.objects.all()
    serializer_class = HighlightedAreaSerializer  
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )