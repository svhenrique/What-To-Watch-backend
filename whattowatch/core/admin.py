
from django.contrib import admin

from core.models import WatchableContent, Episode, HighlightedArea


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ['active', 'id', 'created_at', 'updated_at', 'episode', 'season', 'content']

@admin.register(WatchableContent)
class HighlightedAreaAdmin(admin.ModelAdmin):
    list_display = ['active', 'id', 'created_at', 'updated_at', ]

@admin.register(HighlightedArea)
class HighlightedAreaAdmin(admin.ModelAdmin):
    list_display = ['active','id', 'created_at', 'updated_at', 'position']