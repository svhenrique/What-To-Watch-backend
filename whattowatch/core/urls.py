from django.urls import path
from core import views

urlpatterns = [
    path('episodes/', views.EpisodeList.as_view(), name='episode-list'),
    path('episode/create/', views.EpisodeCreate.as_view(), name='episode-post'),      
    path('episode/read/<int:pk>', views.EpisodeRead.as_view(), name='episode-get'),   
    path('episode/detail/<int:pk>', views.EpisodeDetail.as_view(), name='episode-detail'),

    path('contents/', views.WatchableContentList.as_view(), name='watchablecontent-list'),    
    path('content/create/', views.WatchableContentCreate.as_view(), name='watchablecontent-post'),        
    path('content/read/<int:pk>', views.WatchableContentRead.as_view(), name='watchablecontent-get'),
    path('content/detail/<int:pk>', views.WatchableContentDetail.as_view(), name='watchablecontent-detail'),

    path('highareas/', views.HighlightedAreaList.as_view(), name='HighlightedAreaList-list'),    
    path('higharea/create/', views.HighlightedAreaCreate.as_view(), name='HighlightedAreaList-post'),     
    path('higharea/read/<int:pk>', views.HighlightedAreaRead.as_view(), name='HighlightedAreaList-get'),   
    path('higharea/detail/<int:pk>', views.HighlightedAreaDetail.as_view(), name='HighlightedAreaList-detail'),
]