from rest_framework import serializers
from song.models import Song, Comment


class CommentSerializer(serializers.ModelSerializer):
	'''
	Serializer class for comments on a Song
	'''
	user = serializers.CharField(source='user.get_full_name', read_only=True)
	class Meta:
		model = Comment
		fields = ['id', 'body', 'user', 'created_on']

	read_only_fields = ['user']


class SongListSerializer(serializers.ModelSerializer):
	'''
	Serializer class for Song model. It does not serializes comments. 
	'''
	class Meta:
		model = Song
		fields = ['id', 'title', 'views', 'file']


class SongSerializer(serializers.ModelSerializer):
	'''
	Serializer class for Song model which includes comments on the song as well.
	'''
	comments = CommentSerializer(many=True, read_only=True)

	class Meta:
		model = Song
		fields = ['id', 'title', 'views', 'file', 'comments']


