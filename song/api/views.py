from rest_framework import generics, status
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from song.models import Song
from .serializers import SongSerializer


class SongListAPIView(generics.ListAPIView):
	'''
	Return a list of all the songs
	'''
	serializer_class = SongSerializer
	queryset = Song.objects.all()


class SearchSongAPIView(generics.ListAPIView):
	serializer_class = SongSerializer

	def get_queryset(self):
		''' 
		Filter the queryset based on the title 
		and tag parameters in query string
		'''
		queryset = Song.objects.all()
		title = self.request.query_params.get('title', None)
		tag = self.request.query_params.get('tag', None)

		if title is not None:
			queryset = queryset.filter(title__icontains=title)
		if tag is not None:
			queryset = queryset.filter(tags__icontains=tag)
		return queryset
