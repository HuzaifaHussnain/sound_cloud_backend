from django.urls import path
from .views import (
	SongListAPIView,
	SearchSongAPIView, 
	SongDetailAPIView, 
	CommentCreateAPIView, 
	CommentUpdateAPIView,
	CommentDeleteAPIView,
	LikeSongAPIView,
	RemoveLikeAPIView,
	SongPlayedAPIView,
	)

urlpatterns = [
    path('list/', SongListAPIView.as_view(), name=None),
    path('details/<int:id>', SongDetailAPIView.as_view(), name=None),
    path('search/', SearchSongAPIView.as_view(), name=None),
    path('comment/create/', CommentCreateAPIView.as_view(), name=None),
    path('comment/update/<int:id>', CommentUpdateAPIView.as_view(), name=None),
    path('comment/delete/<int:id>', CommentDeleteAPIView.as_view(), name=None),
    path('like/', LikeSongAPIView.as_view(), name=None),
    path('remove_like/', RemoveLikeAPIView.as_view(), name=None),
    path('increment_view_count/', SongPlayedAPIView.as_view(), name=None)

]
