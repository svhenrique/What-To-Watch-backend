from django.urls import path
from core import views

urlpatterns = [
    path('episode/', views.EpisodeList.as_view(), name='episode-list'),    
    path('episode/<int:pk>', views.EpisodeDetail.as_view(), name='episode-detail'),

    path('content/', views.WatchableContentList.as_view(), name='content-list'),    
    path('content/<int:pk>', views.WatchableContentDetail.as_view(), name='content-detail'),

    path('higharea/', views.HighlightedAreaList.as_view(), name='higharea-list'),    
    path('higharea/<int:pk>', views.HighlightedAreaDetail.as_view(), name='higharea-detail'),
]