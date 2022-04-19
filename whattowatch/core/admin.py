
from django.contrib import admin

from core.models import WatchableContent, Episode, HighlightedArea


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ['active', 'created_at', 'updated_at', 'id', 'episode', 'season']

@admin.register(WatchableContent)
class HighlightedAreaAdmin(admin.ModelAdmin):
    list_display = ['active', 'created_at', 'updated_at', 'id']

@admin.register(HighlightedArea)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ['active', 'created_at', 'updated_at', 'id']