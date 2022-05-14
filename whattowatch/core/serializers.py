from rest_framework import serializers
from core.models import Episode, WatchableContent, HighlightedArea

class EpisodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Episode
        fields = ('name', 'episode', 'content', 'description', 'season', 'video')

class WatchableContentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WatchableContent
        fields = ('title', 'description', 'ratting_age', 'poster',
        'genres', 'release_date', 'daily_views', 'week_views', 'year_views')

class HighlightedAreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HighlightedArea
        fields = ('contents', 'title', 'genres', 'position')