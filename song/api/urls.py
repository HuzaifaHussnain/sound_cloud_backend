from django.urls import path
from .views import SongListAPIView, SearchSongAPIView

urlpatterns = [
    path('list/', SongListAPIView.as_view(), name=None),
    path('search/', SearchSongAPIView.as_view(), name=None)
]
