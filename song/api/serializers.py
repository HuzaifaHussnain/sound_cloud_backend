from rest_framework import serializers
from song.models import Song


class SongSerializer(serializers.ModelSerializer):
	''' Serializer class for Song model '''

	class Meta:
		model = Song
		fields = ['id', 'title', 'views', 'file']