from django.urls import path
from .views import SongListAPIView, SearchSongAPIView, SongDetailAPIView

urlpatterns = [
    path('list/', SongListAPIView.as_view(), name=None),
    path('details/<int:id>', SongDetailAPIView.as_view(), name=None),
    path('search/', SearchSongAPIView.as_view(), name=None)

]
