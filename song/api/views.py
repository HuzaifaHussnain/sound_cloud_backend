from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from song.models import Song, Comment
from .serializers import SongSerializer, SongListSerializer, CommentSerializer


class SongListAPIView(generics.ListAPIView):
	'''
	Return a list of all the songs
	'''
	serializer_class = SongListSerializer
	queryset = Song.objects.all()

class SongDetailAPIView(generics.RetrieveAPIView):
	'''
	Get a single song beased on the id provied
	'''
	serializer_class = SongSerializer
	queryset = Song.objects.all()
	lookup_field = 'id'

class SearchSongAPIView(generics.ListAPIView):
	serializer_class = SongListSerializer

	def get_queryset(self):
		''' 
		Filter the queryset based on the title 
		and tag parameters in query string
		'''
		q = self.request.query_params.get('q', None)

		# return empty result, if no query string is provided for search
		if q is None:
			queryset = None
		else:
			queryset = Song.objects.all()

			# filtering queryset based on the query string q 
			if q:
				queryset = queryset.filter(title__icontains=q) | queryset.filter(tags__icontains=q)
		return queryset


class CommentCreateAPIView(generics.CreateAPIView):
	''' 
	API View to add a comment on a song
	'''
	serializer_class = CommentSerializer
	
	def perform_create(self, serializer):
		song_id = self.request.data['song_id']
		song = get_object_or_404(Song, id=song_id)
		serializer.save(user=self.request.user, song=song)

class CommentUpdateAPIView(generics.UpdateAPIView):
	''' 
	API View to update an existing comment
	'''
	serializer_class = CommentSerializer
	lookup_field = 'id'

	def get_queryset(self):
		user = self.request.user
		return user.comment_set.all()


class CommentDeleteAPIView(generics.DestroyAPIView):
	''' 
	API View to delete the comment from a song
	'''
	serializer_class = CommentSerializer
	lookup_field = 'id'

	def get_queryset(self):
		user = self.request.user
		return user.comment_set.all()


class LikeSongAPIView(APIView):
	'''
	This view will add a like to a song
	'''
	def post(self, request):
		song_id = request.POST.get('song_id')
		user = request.user
		song = get_object_or_404(Song, id=song_id)
		data = {}
		if user not in song.likes.all():
			song.likes.add(user)		
		data['likes_count'] = song.likes.count()
		data['liked_by_user'] = True

		return Response(data, content_type='application/json')

class RemoveLikeAPIView(APIView):
	'''
	This view will remove the user's like from the song
	'''
	def post(self, request):
		song_id = request.POST.get('song_id')
		user = request.user
		song = get_object_or_404(Song, id=song_id)
		data = {}
		if user in song.likes.all():
			song.likes.remove(user)		
		data['likes_count'] = song.likes.count()
		data['liked_by_user'] = False

		return Response(data, content_type='application/json')


